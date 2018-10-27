#include <iostream>
using namespace std; 

int main()
{
	
	int sum5 = 0; 
	int sum3 = 0; 
	int i = 1; 

	for (int mul5 = 5 ; mul5 < 1000; mul5 = 5*i) 
	{	
		if (mul5%3 != 0 )
		{	cout<< sum5; 
			sum5 = sum5 + mul5; 	
			cout << "+" << mul5 << "=" << sum5 << " ";  
		}
		i++;
	
	}  
	i = 1; 
	cout << endl; 
	
	for (int mul3 = 3 ; mul3 < 1000; mul3 =3*i) 
	{
		cout<< sum3; 
		sum3 = sum3 + mul3; 
		cout << "+" << mul3 << "=" << sum3 << " ";  
		i++;
		
	}  
	 
	cout << "the sum of all the multiples of 3 or 5 below 1000 is " << sum3+sum5 << endl ;
	
	
	return 0;
}
