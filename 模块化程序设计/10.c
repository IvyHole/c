#include<stdio.h>
int fibonacci(int);
int sum2(int);
int fibonacci(int x){
	if (x==1 || x==2){
		return 1;
	}else{
		return fibonacci(x-1) + fibonacci(x-2);
	}
}
int sum2(int n){
	int s=0,i;
	for (i=1;i<=n;i++){
		s=s+fibonacci(i);
	}
	return s;
}
int main(){
	printf("%d",sum2(20));
	return 0;
}