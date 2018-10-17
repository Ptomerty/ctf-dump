#include <stdio.h>

void thing(int a, int b, int c) {
	__asm__("mov $0x27,%eax; xor	%al,%al; mov	11(%ebp), %ah; sal	$0x10,%ax; sub	12(%ebp), %al; add	15(%ebp), %ah; xor	18(%ebp), %ax ");

}

int main() {
//	uint32_t b = 0xaee1f319;
//	b = b << 16;
//	b = b - 0xe1f319;
//	b = b + 0xe0911505;
//	b = b ^ 0xfac0f685;
//	printf("%x", b);
	thing(0xfac0f685, 0xe0911505, 0xaee1f319);
	return 0;
}
