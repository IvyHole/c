#include<stdio.h>
int isPrime(){
	int n,i,j=0,id;
	printf("Please input a number:");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{	
		if (n%i==0){
			j++;
		}
		if (j>2){
			id=0;
			break;
		}
	}
	if (id==0){
		printf("It is not a Prime\n");
	}else{
		printf("It is a Prime\n");
	}
	return 0;
}
int flower(){
	int n;
	printf("Please input a number:");
	scanf("%d",&n);
    if((n/100)*(n/100)*(n/100)+(n/10%10)*(n/10%10)*(n/10%10)+(n%10)*(n%10)*(n%10)==n)
		printf("It is a narcissistuc number\n");
	else
		printf("It is not a narcissistuc number\n");
	return 0;
}
int divisor(){
	int n,m;
	printf("Please input two numbers(a b):");
	scanf("%d %d", &n, &m);
	int i=n>m?m:n;
	while(1==1){
		if (n%i==0 && m%i==0){
			printf("divisor = %d\n",i);
			break;
		}
		i--;
	}
	return 0;
}
int fibonacci(int x){
	if (x==1 || x==2){
		return 1;
	}else{
		return fibonacci(x-1) + fibonacci(x-2);
	}
}
int fibonaccis(){
	int i,j,n;
	printf("Please input a number:");
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		printf("%-5d",fibonacci(i));
	}
	printf("\n");
	return 0;
	
}
int main(){
	int iSwitch;
	while(1==1){
	printf("\n**********************************");
	printf("\n* Menu section                   *");
	printf("\n* 1. 素数判断                    *");
	printf("\n* 2. 求‘水仙花’数              *");
	printf("\n* 3. 求最大公约数                *");
	printf("\n* 4. 斐波那契数列                *");
	printf("\n* 5. Exit                        *");
	printf("\n**********************************\n\n");
	scanf("%d",&iSwitch);
	switch(iSwitch){
		case 1: isPrime();break;
		case 2: flower();break;
		case 3: divisor();break;
		case 4: fibonaccis();break;
		case 5: goto back;break;
		default:;
	}
	}
	back: return 0;
}