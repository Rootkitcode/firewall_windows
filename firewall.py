import os
import platform

#R4c0d3 @Author
#Check if we are runing on a windows-based operating system

if platform.system() == "Windows":
    # Run the "netsh" command to view the firewall rules
    output = os.popen("netsh advfirewall show allprofiles").read()
    #our output
    print(output)