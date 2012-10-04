/*************
 * = mergesort.c
 * an improved version of mergesort
 * (compare to my last implementation)
 * improvements based on the stuff taught in one lecture
 * Po Chen
 * 2012-8-24
 *************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
	int usage, max;
	int *vs;
} storage;

void add( storage *, int );
void init( storage * );
void mergesort( int*, int );
void recurcall( int*, int, int*, int, int* );

int main( int argc, char const *argv[] ) {
	int n;
	// int t1, t2;
	storage st;
	init( &st );
	while( scanf( "%d", &n ) == 1 )
		add( &st, n );
	// t1 = clock();
	mergesort( st.vs, st.usage );
	// t2 = clock();
	// printf("%d %d, %d\n", t1, t2, t2-t1);
	for( n = 0; n < 100; n++ )
		printf( "%d ", st.vs[n] );
	putchar( '\n' );
	for( n = st.usage - 100; n < st.usage; n++ )
		printf( "%d ", st.vs[n] );
	putchar( '\n' );
	return 0;
}

void mergesort( int *arr, int n ){
	int *temp = (int*) malloc(sizeof(int)*n);
	int h = n/2;
	recurcall( arr, h, arr+h, n-h, temp );
}

void recurcall( int *first, int n1, int *second, int n2, int *temp ){
	int h, total = n1+n2;
	int *start = first;
	if(n1>1){
		h = n1/2;
		recurcall( first, h, first+h, n1-h, temp );
	}
	if(n2>1){
		h = n2/2;
		recurcall( second, h, second+h, n2-h, temp );
	}
	while( n1+n2>0 ){
		if( n1 && n2 ){
			if( *first<*second ){
				*temp++ = *first++;
				n1--;
			}else{
				*temp++ = *second++;
				n2--;
			}
		}else if(n1){
			while(n1--)
				*temp++ = *first++;
		}else{
			while(n2--)
				*temp++ = *second++;
		}
	}
	temp -= total;
	for(;total>0;total--)
		*start++ = *temp++;
}

void init( storage *st ){
	st->max = 1024;
	st->usage = 0;
	st->vs = ( int * )malloc( sizeof( int )*st->max );
}

void add( storage *st, int v ){
	if( ( st->usage+2 )>st->max ){
		st->max *= 2;
		st->vs = ( int * )realloc( st->vs, sizeof( int )*st->max );
	}
	st->vs[st->usage++] = v;
}