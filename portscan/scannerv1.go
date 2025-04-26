package main

import (
	"flag"
	"fmt"
	"net"
	"os"
)

func main() {

	ip := flag.String("ip", "", "Target IP address to scan")

	//Usage: go run gortscan.go -ip
	flag.Usage = func() {
		fmt.Println("Usage: gortscan -ip <Target IP>")
		flag.PrintDefaults()
	}
	// Parse the command line flags
	flag.Parse()

	// Check if the IP address is provided
	if flag.NArg() == 0 {
		flag.Usage()
		// Bad exit
		os.Exit(1)
	}

	for i := 1; i < 1024; i++ {
		_, err := net.Dial("tcp", fmt.Sprintf("%v:%d", ip, i))

		if err != nil {
			fmt.Printf("Port %d is closed...\n", i)
		} else {
			fmt.Printf("Port %d is open...\n", i)
		}
	}
}
