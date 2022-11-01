#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#pragma warning(disable:4996)

int* sub_arr(int* arr, size_t len) {

	int* sub_arr = (int*)malloc(len * sizeof(int));
	for (size_t i = 0; i < len; i++) {
		sub_arr[i] = arr[i] / abs((arr[i]));
	}
	return sub_arr;
}

_Bool check_arr(int* arr, size_t len) {
	for (size_t i = 1; i < len - 1; i++) {
		if (arr[i] == arr[i - 1]) {
			return 0;
		}
	}
	return 1;
}

void printArr(int* arr1, size_t len) {
	for (size_t i = 0; i < len; i++) {
		printf(" %d ", arr1[i]);
	}
}

int main() {
	size_t len1 = 5;
	size_t len2 = 8;

	int arr1[] = {1, 2, 3, 4, 5};
	int arr2[] = { 1, -1, 2, -2, 3, -3, 4, -4 };

	int* sub1 = sub_arr(arr1, len1);
	printArr(sub1, len1);

	int* sub2 = sub_arr(arr2, len2);
	printf("\n");
	printArr(sub2, len2);
	
	printf("\n");

	_Bool val1 = check_arr(sub1, len1);
	_Bool val2 = check_arr(sub2, len2);
	printf("%d\n", val1);
	printf("%d", val2);

}
