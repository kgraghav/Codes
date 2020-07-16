// MyProject2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include<conio.h>
#include<math.h>
#include<fstream>

using namespace std;

float u(float x, float t, float u1, float u2, float tol) // u(..) SOLVER function..
{
	float speed;											
	if ((u1 - 1 - sin(x - u1 * t)) * (u2 - 1 - sin(x - u2 * t)) > 0)	
			// If initial guesses of approx. have same sign
	{		// shift limits
		if ((u1 - 1 - sin(x - u1 * t)) > 0)// according to whether root is > or < approx. range.
		{
			while ((u1 - 1 - sin(x - u1 * t)) * (u2 - 1 - sin(x - u2 * t)) > 0)
			{
				float a = u1;
				u1 = 2 * u1 - u2;
				u2 = a;
			}
		}
		else if ((u2 - 1 - sin(x - u2 * t) < 0))
		{
			while ((u1 - 1 - sin(x - u1 * t)) * (u2 - 1 - sin(x - u2 * t)) > 0)
			{
				float b = u2;
				u2 = 2 * u2 - u1;
				u1 = b;
			}
		}
	}
	while (u2 - u1 > tol)	// While limits are not within tolerance,	
	{
		float u3;
		u3 = u1;		// store initial u1 in a dummy variable.		
		u1 = (u1 + u2) / 2;	 // Shift u1 by the average of u1 and u2.	       
		if ((u1 - 1 - sin(x - u1 * t)) * (u2 - 1 - sin(x - u2 * t)) > 0)					  // If u1 and u2 do not enclose root,					{		  // Shift interval towards u1.
		{
			u2 = u1;
			u1 = u3;
		}

	}
	speed = ((u1 + u2) / 2);
			return speed;	// Return (u1+u2)/2 to ensure it is within tolerance.
}
float uvel(float x, float t, float u1, float u2, float tol)// uvel(..) SOLVER function 
{
	while (u2 - u1 > tol)	     // While limits are not within tolerance,
	{
		float u3;	    // store initial u1 in a dummy variable.	
		u3 = u1;
		u1 = (u1 + u2) / 2;   // Shift u1 by the average of u1 and u2.	       
		if ((u1 - 1 - sin(x - u1 * t)) * (u2 - 1 - sin(x - u2 * t)) > 0)					   	// If u1 and u2 do not enclose root,				{		  	// Shift interval towards u1.
		{
			u2 = u1;
			u1 = u3;
		}
	}
	return (u1 + u2) / 2;
}

int main()
{
	float xi, ti, u1, u2, tol, time;
	cout << "This compiler compiles using bisection method." << endl;
	cout << "Enter the values for initial smallest x, initial t,lower limit of approximation, upper limit of approximation, tolerance, final time step in that order." << endl;
	cin >> xi >> ti >> u1 >> u2 >> tol >> time;
	ofstream MyExcelFile;

	if (u1 < u2 && time >= ti)	  // Solve for u using limits as input.
	{
		MyExcelFile.open("cfdPhw1.csv");
		float vel[201], x[201];
		cout << endl;
		cout << "The distribution of velocity with distance and time (in steps of 0.5 seconds) is as given:" << endl;
		for (int j = 1; j < 102; j++) // Loop to produce first set of t, x and u values
		{
			x[j] = xi + (j - 1) * (6.2831853) / 100;
			vel[j] = u(x[j], ti, u1, u2, tol);
		}
		for (int j = 1; j < 102; j++) // Loop to display first set of t, x and u values
		{
			MyExcelFile << ti << "," << x[j] << "," << vel[j] << endl;
		}
		MyExcelFile << endl;
		for (float t = ti + 0.5; t <= time; t = t + 0.5)								// Makes further loops based on x=xinitial+uinitial*tpresent	
		{
			float dis, v[201];
			dis = x[1] + vel[1] * t;
			v[1] = u(dis, t, vel[1] - 0.1, vel[1] + 0.1, tol);
			MyExcelFile << t << "," << dis << "," << v[1] << endl;									// Output first set of x and u values.
			for (int n = 2; n < 102; n++)							// Loop to output remaining x and u values for any t.
			{
				dis = x[n] + vel[n] * t;
				if (n > 2)
				{
					if (v[n - 1] - v[n - 2] > 0)						// If increasing function, take limits as previous u, previous u + 0.01.
					{
						v[n] = u(dis, t - ti, v[n - 1], v[n - 1] + 0.01, tol);
					}
					else							// Otherwise take limits as respective u in first loop(vel [n]-0.001,vel[n] 
					{		// Use function uvel(..).
						v[n] = uvel(dis, t - ti, vel[n] - 0.01, vel[n], tol);
					}
				}
				else
				{
					v[n] = u(dis, t - ti, v[n - 1], v[n - 1] + 0.01, tol);
				}
				MyExcelFile << t << "," << dis << "," << v[n] << endl;									// Display t, x and u values.					}
				MyExcelFile << endl;
			}
		}
	}
	else
	{
		cout << "Invalid Limits." << endl << endl;						// If u1<u2 and ti<time is not true, output "Invalid Limits".	
	}
	MyExcelFile.close();
	return 0;
}





// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
