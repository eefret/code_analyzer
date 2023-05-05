package main

import "fmt"

func main() {
	var a int
	fmt.Println("Enter an integer: ")
	fmt.Scanf("%d", &a)
	if a%2 == 0 {
		fmt.Println("The integer is even.")
	} else {
		fmt.Println("The integer is odd.")
	}
}
