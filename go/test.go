package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var n, t int
	fmt.Sscanf(scanner.Text(), "%d %d", &n, &t)

	scanner.Scan()
	letters := strings.Split(scanner.Text(), " ")

	for i := 0; i < t; i++ {
		scanner.Scan()
		pin := scanner.Text()

		if !isValidPIN(pin, letters) {
			fmt.Println("NO")
			continue
		}

		if !isPermutation(pin, letters) {
			fmt.Println("NO")
		} else {
			fmt.Println("YES")
		}
	}
}

func isValidPIN(pin string, letters []string) bool {
	letterMap := make(map[rune]bool)
	for _, letter := range letters {
		letterMap[rune(letter[0])] = true
	}

	for _, char := range pin {
		if !letterMap[char] {
			return false
		}
	}
	return true
}

func isPermutation(pin string, letters []string) bool {
	pinLetters := make([]rune, len(pin))
	for i, char := range pin {
		pinLetters[i] = char
	}

	sort.Slice(pinLetters, func(i, j int) bool {
		return pinLetters[i] < pinLetters[j]
	})
	sort.Strings(letters)

	for i, letter := range letters {
		if rune(letter[0]) != pinLetters[i] {
			return false
		}
	}
	return true
}
