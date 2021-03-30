#include <iostream>
using namespace std;
int prime(int n,int i){
	if (n <= 2)
        return (n == 2) ? 1 : 0; 
    if (n % i == 0) 
        return 0; 
    if (i * i > n) 
        return 1; 
    return prime(n, i + 1); 
}
int main() {
	int t,n;
	cin>>t;
	while(t--){
	    cin>>n;
	    if(prime(n,2)) cout<<"yes"<<endl;
	    else cout<<"no"<<endl;
	}
	return 0;
}
