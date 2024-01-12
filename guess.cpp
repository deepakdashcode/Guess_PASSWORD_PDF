#include<iostream>
using namespace std;
int main(){
int password = 1237;

int guess = 0;
while(guess != password){
cout << "Guess the password : ";
cin>>guess;
if(guess == password){
cout << "Correct Guess\n";
break;
}
else if(guess > password)
    cout << "Lower\n";
else
    cout << "Higher\n";
}
//MyReadFile.close();
system("pause");
return 0;
}