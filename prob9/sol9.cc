#include <iostream>
#include <cmath>
using namespace std; 

int main()
{
	int one= 0; 
	int two  =0; 
	int three = 0; 
	
	for (int a = 0; a < 1000; a++)
	{
		for (int b = 0; b < 1000; b++)
		{ 
			if (a<b)
			{
				
				for (int c = 0; c < 1000; c++)
				{
					if ( b < c)
					{
						if (((a + b + c )==1000) && ( a*a + b*b == c*c ))
						{
							one = a; 
							two = b; 
							three = c; 
							
							cout << "a = " << a << " , b = " << b; 
							cout << ", c = " << c << endl; 
						}
					}
				}
			}
		}
	}
	
	cout << "-------> your answer is : " << one*two*three << endl; 
	
	return 0; 
}
