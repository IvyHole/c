#include <stdio.h>
int isPrime(int n){
	int i,j=0;
	for(i=1;i<=n;i++)
	{	
		if (n%i==0){
			j++;
		}
		if (j>2){
			return 0;
		}
	}
	return 1;
}
int main(){
	int i;
	for(i=100;i<=200;i++){
		if(isPrime(i)){
			printf("%d is prime!\n",i);
		}
	}
}