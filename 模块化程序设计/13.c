#include<stdio.h>
#include<math.h>
int factn(int a, int b){
	int i,sum=0;
	for (i=1;i<=b;i++){
		sum=sum+pow(a,i);
	}
	return sum;
}
int main(){
	int x,n;
	scanf("%d %d", &x,&n);
	printf("%d",factn(x,n));
}