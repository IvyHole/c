#include <stdio.h>
int n,m;
int divisor(){
	int i=n>m?m:n;
	while(1==1){
		if (n%i==0 && m%i==0){
			return i;
		}
		i--;
	}
}
int multiple(){
	int i=n>m?n:m;
	while(1==1){
		if (i%n==0 && i%m==0){
			return i;
		}
		i++;
	}
}
int main(){
	scanf("%d %d", &n, &m);
	printf("divisor=%d,multiple=%d",divisor(n,m),multiple(n,m));
}