#include <iostream>
#include <cmath>

using namespace std; 

int main()
{
	
	int sqr =0; 
	int sum = 0; 
	
	for (int i = 1; i <=100; i++)
	{
		sum = sum + i; 
		sqr = sqr + i*i; 
	}
	sum = sum*sum;
	
	cout << "sum of the squares of the first one hundred natural numbers: " << sqr << endl; 
	cout << "square of the sum of the first one hundred natural numbers: " << sum << endl; 
	cout << "---> difference: " << sum-sqr << endl; 

	return 0;
}
