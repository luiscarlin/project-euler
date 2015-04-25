#include <iostream>
#include <vector> 

using namespace std; 
int main()
{
	vector <int> primes;
	primes.push_back(2); 
	
	
	int i = 3; 
	
	while (primes.size() != 10001)
	{
		bool itIs = true; 
		
		for (int k = 2; ((k<i)&&(itIs==true)) ; k++)
		{
			if (i%k == 0)
				itIs = false; 
		}
		if (itIs == true)
		{
			cout << "found prime: " << i << endl; 
			primes.push_back(i); 
		}
		i++; 
	}
	
	cout << primes[10000] << " is the 10001st prime" << endl; 
	
	return 0; 
}
