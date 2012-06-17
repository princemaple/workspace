#include <stdio.h>
#include <stdlib.h>

void perms(int);
void callee(int *, int);
void prt(int *);

int main(void){
	int n, c;
	while((c=scanf("%i", &n))==1){
		perms(n);
	}
	return 0;
}

void perms(int n){
	int i, nums[n+1];
	for(i=0;i<=n;i++){
		nums[i]=n-i;
	}
	callee(nums, n);
}

void callee(int *nums, int n){
	if(n>1){
		int i;
		for(i=0;i<n;i++){
			callee(nums, n-1);
			if(i<n-1){
				if(n%2){
					nums[0]^=nums[n-1];
					nums[n-1]^=nums[0];
					nums[0]^=nums[n-1];
				}else{
					nums[i]^=nums[n-1];
					nums[n-1]^=nums[i];
					nums[i]^=nums[n-1];
				}
			}
		}
	}
	else
		prt(nums);
}

void prt(int *nums){
	int i=0;
	while(*nums){
		nums++;
		i++;
	}
	while(i--)
		printf("%3d", *(--nums));
	putchar('\n');
}
