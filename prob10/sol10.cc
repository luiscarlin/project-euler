#include <iostream> 
#include <vector>
#include <cmath>
using namespace std; 

int main()
{
	unsigned long long sum = 2; 
	
	unsigned long long int limit = 2000000; 
	
	for (unsigned long long  i = 3; i <= limit; i++) 
	{
		if ( i%2 !=0)
		{
			bool prime = true;
			for ( unsigned long long k = 2; (k<i) && (prime ==true); k++)
			{
				if (i%k == 0)
				{
					prime = false; 
				}
			}
		
			if (prime == true)
			{
				cout << "Found prime : " << i << endl; 
				sum = sum + i; 
			}
		}
	}
	
	cout << "-----> The sum of the primes under " << limit << " is: " << sum << endl; 
	
	return 0; 
}
