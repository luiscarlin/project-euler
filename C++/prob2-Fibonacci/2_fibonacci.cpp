#include <iostream>
using namespace std; 

int main()
{
	
	int num_2 = 1; 
	int num_1 = 2; 
	
	int sum = 2; //2 from the start
	
	for (int num = 3; num<4000000; num = num_2 + num_1)
	{
		if (num%2 == 0)
		{ 
			sum = sum + num; 
		}
		num_2 = num_1; 
		num_1 = num;   
	}
	cout << "The sum of all the even-valued terms in the sequence which do not exceed four million is " << sum << endl; 
	
	return 0;
}
