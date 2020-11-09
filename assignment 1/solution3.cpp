#include<iostream>
#include<string.h>
using namespace std;



int main() {

   int a,b;
   cout<<"ENTER LIMIT 1 PRESS ENTER/SPACE ENTER LIMIT 2: "<<"\n";
   cin>>a>>b;
   cout<<"THE PRIME NUMBERS ARE: "<<"\n";
   for(int i=a;i<= b ; i++)
   {
      bool isPrime = 1;
       for(int j=2;j<i;j++)
       {
           if(i%j==0)
           {
               isPrime=0;
           }
       }
       if(isPrime)
       {
           cout<<i<<"\n";
       }
   }
	return 0;
}