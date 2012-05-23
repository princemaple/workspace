/*this program is designed to remove all the comments in
  C and C++ or any other programming language that uses "//" and
  "/ * * /" (without white spaces) as comment*/
#include <stdio.h>

#define enable 1
#define disable 0
int main(void){
	char c, buf=0;
	//style1="//" style2="/**/"
	char style1=disable, style2=disable;
	char output=enable;
	while((c=getchar())!=EOF){
		if(c=='/' && !buf && !style1 && !style2){
			buf=c;
			continue;
		}else if(c=='/' && buf=='/'){
			buf=0;
			style1=enable;
			output=disable;
			continue;
		}else if(c=='/' && buf=='*' && style2){
			buf=0;
			style2=disable;
			output=enable;
			continue;
		}else if(c=='*' && buf=='/' && !style1 && !style2){
			buf=0;
			style2=enable;
			output=disable;
			continue;
		}else if(c=='*' && !buf && style2){
			buf=c;
			continue;
		}
		if(c=='\n' && style1){
			style1=disable;
			output=enable;
		}
		if(output){
			if(buf){
				putchar(buf);
				buf=0;
			}
			putchar(c);
		}
	}
	return 0;
}