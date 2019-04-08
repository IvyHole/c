#include <stdio.h>
int divisor(int n,int m){
	int i=n>m?m:n;
	while(1==1){
		if (n%i==0 && m%i==0){
			return i;
		}
		i--;
	}
}
int multiple(int n,int m){
	int i=n>m?n:m;
	while(1==1){
		if (i%n==0 && i%m==0){
			return i;
		}
		i++;
	}
}
int main(){
	int a,b;
	scanf("%d %d", &a, &b);
	printf("divisor=%d,multiple=%d",divisor(a,b),multiple(a,b));
}