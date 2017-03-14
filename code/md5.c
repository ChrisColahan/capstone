//MD5 implementation
//reference from Applied Cryptography by Bruce Schneier

#include "stdio.h"
#include "string.h"
#include "stdlib.h"

//takes a message m as imput
unsigned char* MD5(unsigned char in_m[]) {
	//padding
	long origlen = strlen(in_m);
	long numzeros = 513 - (strlen(in_m)+63 % 512);
	long newlen = origlen+1+numzeros+64+1;
	char *m = (char*) malloc(newlen);
	m[origlen] = 1;
	printf(newlen, "%d\n");
	for(int i = 0; i < numzeros; i ++) {
		m[origlen+1+numzeros]=0;
	}
	m[newlen-1]='\0';
	
	return m;
}

int main() {
	char in[] = "password";
	printf(in, "%s\n");
	char* m = MD5(in);
	printf(m, "%s\n");
	free(m);
}
