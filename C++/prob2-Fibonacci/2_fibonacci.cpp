//      2_fibonacci.cpp
//      
//      Copyright 2010 Luis Carlin <luis@luis-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


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
