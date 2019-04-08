#include<stdio.h>
void fun();
void fun(){
	static int x=1;
	int y=10;
	x=x+2;
	y=y+x;
    printf("%d %d",x,y);
}
int main(){
	int x=2,y=3;
	printf("%d %d",x,y);
	fun();
	printf("%d %d",x,y);
fun();}