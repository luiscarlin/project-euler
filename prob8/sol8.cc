#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
	vector<int> in; 
	vector<int> five; 
	
	int num; 
	ifstream infile; 
	infile.open( "file.txt" ); 
	
	num = infile.get();
	
	while (infile)
	{ 
		num = num-48; 
		in.push_back(num); 
		
		num = infile.get(); 
	}
	
	infile.close(); 
	
	for ( unsigned i = 4; i < in.size(); i++)
	{
		five.push_back(in[i-4]*in[i-3]*in[i-2]*in[i-1]*in[i]); 
	}
	
	int max = 0; 
	
	if (five.size()>1)
	{
		max = five[0]; 
	}
	for( unsigned i = 0; i < five.size(); i++)
	{
		if( five[i] > max)
		max = five[i]; 
	}
	cout << max << endl; 
	return 0; 
} 
