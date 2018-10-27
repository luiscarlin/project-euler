#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>

using namespace std; 

int main()
{
	vector <int> palindromes; 
	for (int i = 999; i >= 100; i--)
	{
		for (int k = 999; k >= 100; k--)
		{
			int result = i*k; 
			string str;
	
			stringstream out;
			
			out << result;
	
			str = out.str();
 
			if ((str.size() == 5)&&(str[0]==str[4])&&(str[1]==str[3]))
				cout << "found a palindrome: " << i << "x" << k << " = " << str << endl;
			
			if ((str.size() == 6)&&(str[0]==str[5])&&(str[1]==str[4])&&(str[2]==str[3]))
			{
				cout << "found a palindrome: " << i << "x" << k << " = " << str << endl;
				palindromes.push_back(i*k);
			}
		}
	}
	int max; 
	if (palindromes.size() > 1)
		max = palindromes[0]; 
	
	for ( unsigned  int i= 0; i < palindromes.size(); i++)
	{
		if (palindromes[i] > max)
		max = palindromes[i];
	}
			
	cout << "---> The greatest Palindrome is: " << max << endl; 
	return 0; 
}
