#include <iostream> 
#include <vector>
#include <cmath>
using namespace std; 

bool isThere(vector<unsigned long long int> vec, unsigned long long int prime)
{
	bool toRet = false; 
	for (int i = 0; i < vec.size(); i++)
	{
		if (vec[i] == prime)
		toRet = true; 
	} 
	return toRet; 
} 

void divide (unsigned long long int toDiv, unsigned long long int prime, vector <unsigned long long int> &primeVec) 
{
	if ( toDiv != 1 )
	{
		cout << "TRYING: " << toDiv << " and " << prime << endl; 
		if ( toDiv% prime != 0)
		{
			divide( toDiv, prime+1, primeVec);  
		} 
		else
		{
			if (!(isThere(primeVec, prime)))
			{
				cout << "!FOUND PRIME: " << prime << endl; 
					primeVec.push_back(prime); 
			}
			toDiv = toDiv/prime; 
			divide (toDiv, prime, primeVec);

		}
	}
	else 
	{
		return; 
	} 
}

int main()
{

	vector <unsigned long long int> primes; 
	unsigned long long int num = 60; //600851475143LL;
	unsigned long long int first = 2; 
	divide ( num, first, primes); 

	for( int i = 0; i< primes.size(); i++) 
		cout << primes[i] << endl; 
//	cout << "The largest prime factor of the number 600851475143 is: " << max << endl;
	
	return 0; 

}
