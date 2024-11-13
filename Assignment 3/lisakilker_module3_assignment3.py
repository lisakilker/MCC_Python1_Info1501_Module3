#imports regular expressions library
import re

#Program will pull IP addresses from error_log.txt file and list them in a column in the ip_address.txt file
def main():

    #Define the regular expression pattern for IPv4 addresses
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

    #Open the file to read from
    read_file = open("error_log.txt", "r")
    #Open the file to write to
    write_file = open("ip_address.txt","w")
    #Adds a header on the top of the file that says "IP Addresses"
    write_file.write("IP Addresses:\n")

    #Loop through the file object, one line at a time
    for line in read_file:
        #Only process lines that aren't blank
        if line.strip():
            #Look for IPv4 addresses on each line
            result = ipv4_pattern.findall(line)
            #Don't print if the result is an empty list
            for ip in result:
                    write_file.write(ip + "\n")

    #Closes the files
    read_file.close()
    write_file.close()

#Calls the main function
if __name__ == "__main__":
    main()

