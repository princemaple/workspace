/*************
 * = merge.c
 * a practice work
 * trying to code a merge sort
 * succeeded
 * Po Chen
 * 2012-8-13
 *************/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int usage, max;
	int *vs;
} storage;

int *split( int *, int );
int *merge( int *, int, int *, int );
void callmerge( int *, int );
void add( storage *, int );
void init( storage * );

int main( int argc, char const *argv[] ) {
	int n;
	storage st;
	init( &st );
	while( scanf( "%d", &n ) == 1 )
		add( &st, n );
	callmerge( st.vs, st.usage );
	for( n = 0; n < st.usage; n++ )
		printf( "%d ", st.vs[n] );
	putchar( '\n' );
	return 0;
}

void init( storage *st ){
	st->max = 8;
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

void callmerge( int *a, int n ){
	int *p = split( a, n );
	int i;
	for( i = 0; i<n; i++ )
		a[i] = p[i];
}

int *merge( int *a, int n1, int *b, int n2 ){
	if( n1>1 )
		a = split( a, n1 );
	if( n2>1 )
		b = split( b, n2 );
	int i = 0, *arr = ( int * )malloc( sizeof( int )*( n1 + n2 ) );
	while( ( n1 + n2 ) > 0 ){
		if( n1>0 && n2>0 ){
			if( *a<*b ){
				arr[i++] = *( a++ );
				n1--;
			}
			else{
				arr[i++] = *( b++ );
				n2--;
			}
		}else{
			if( n1>0 ){
				arr[i++] = *( a++ );
				n1--;
			}else{
				arr[i++] = *( b++ );
				n2--;
			}
		}
	}
	if( n1>1 )free( a );
	if( n2>1 )free( b );
	return arr;
}

int *split( int *a, int n ){
	int h = n/2;
	return merge( a, h, a+h, n-h );
}