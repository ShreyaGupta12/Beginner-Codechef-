#include <iostream>
using namespace std;

int main() {
	double w,a;
	cin>>w>>a;
	a=((a<(w+0.50))||((int(w)%5)!=0))?a:(a-(w+0.50));
	cout<<a;
	return 0;
}
