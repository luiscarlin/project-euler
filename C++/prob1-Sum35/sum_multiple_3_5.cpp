//      test.cpp
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
