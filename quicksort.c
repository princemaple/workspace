/*************
 * = quicksort.c
 * practice work
 * trying to implement quicksort
 * succeeded
 * Po Chen
 * 2012-8-18
 *************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
	unsigned int usage, max;
	int *vs;
} storage;

void add( storage *, int );
void init( storage * );
void callquicksort( int *, unsigned int );
void swap( int*, int* );

int main( int argc, char const *argv[] ) {
	int n;
	storage st;
	init( &st );
	// int t1, t2;
	while( scanf( "%d", &n ) == 1 )
		add( &st, n );
	// printf( "%d\n", st.usage );
	// t1 = clock();
	callquicksort( st.vs, st.usage );
	// t2 = clock();
	// printf("%d %d %d\n", t1, t2, t2 - t1);
	// for( n = 0; n < 100; n++ )
	// 	printf( "%d ", st.vs[n] );
	// putchar( '\n' );
	// for( n = st.usage - 100; n < st.usage; n++ )
	// 	printf( "%d ", st.vs[n] );
	// putchar( '\n' );
	return 0;
}

void callquicksort( int *arr, unsigned int n ){
	// printf( "called %d\n", n );
	if( n <= 1 )return;
	int pivot = arr[0];
	int left = 1, right = n-1;
	// printf( "%d\n", right );
	while( right>left ){
		while( arr[left]<=pivot )
			left++;
		while( arr[right]>pivot )
			right--;
		if( right>left )
			swap( arr+left, arr+right );
		else
			break;
	}
	if( pivot > arr[right] ){
		swap( arr, arr + right );
		callquicksort( arr, right + 1 );
	}
	callquicksort( arr + left, n - left );
}

void swap( int *a, int *b ){
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
}

void init( storage *st ){
	st->max = 1024;
	st->usage = 0;
	st->vs = ( int * )malloc( sizeof( int )*st->max );
	// printf("inited\n");
}

void add( storage *st, int v ){
	if( ( st->usage+2 )>st->max ){
		st->max *= 2;
		st->vs = ( int * )realloc( st->vs, sizeof( int )*st->max );
	}
	st->vs[st->usage++] = v;
	// printf( "added %d, usage %d, max %d\n", v, st->usage, st->max );
}