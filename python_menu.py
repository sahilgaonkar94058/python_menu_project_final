import os
import time
import getpass
import subprocess

#FUNCTIONS
#SUB CODES

#YUM CONFIGURATION
def yum_conf():
    path = '/etc/yum.repos.d/conf.repo'
    f = open(path,'w')
    try:
        f.writelines('''[dvd1]
baseurl = file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/AppStream
gpgcheck = 0

[dvd2]
baseurl = file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/BaseOS
gpgcheck = 0''')
    except:
        print('failed!!')
    else:
        print('succeeded!!')
    finally:
        f.close()

#WEB PAGE CREATION
def web_test():

    path = '/var/www/html/test.html'
    f = open(path,'w')
    try:
        f.writelines('''<!DOCTYPE html>
<html>
<head>
<style>
body{
    background-color: #E6E6FA
}
</style>
</head>
<body>
<h1>test webpage!!</h1>
</body>
</html>''')
    except:
        print('failed!!')
    else:
        print('web page created!!')
    finally:
        f.close()

#IP
def ip():
    localip = subprocess.getoutput(" ifconfig enp0s3 | grep -w inet | awk '{print $2}' ")
    print('The current machine IP is : {} '.format(localip))





#MAIN_MENU
os.system('tput setaf 4')
print('\t\t\tPython Automation System')
os.system('tput setaf 3')
print('\t\t------------------------------------')
os.system('tput setaf 6')


count = 0

while  count < 2:
    user_id = input('User ID (admin): ')
    passwd = getpass.getpass('password (admin) : ')
    if user_id=='admin' and passwd=='admin':
        print('Access granted')
        break
    else:
        print('Access denied')
        count+=1
        if count==2:
            exit()

os.system('tput setaf 7')

while True:
    os.system("tput setaf 3")
    print("\t\tServices")
    os.system("tput setaf 4")
    print("\t----------------")
    os.system("tput setaf 6")

    ip()

    print("""
    0. Exit
    1. Linux(Red Hat)
    2. Hadoop
    3. AWS
    4. Docker
    """)

    option = input("select an option: ")

    if option == "0":
        os.system("tput setaf 7")
        exit()
    elif option == "1":
        while True:
            print("RHEL")
            print("------")
            ip()
            print("""
            0. Back to previous menu
            1. Display date
            2. Display Cal
            3. Open manual of any command
            4. List directory content
            5. Create a directory
            6. Remove a directory
            7. Change directory
            8. back to / or default directory
            9. Create an empty file
            10. Create and open a new file for editing
            11. Add a new user
            12. Set/Change password of a user
            13. List all users
            14. Configure yum repolist
            15. Display yum repolist
            16. Display information about the CPU architecture
            17. Display amount of free and used memory in the system(in mebibytes)
            18. Report file system disk space usage
            19. Display the status of the currently active network interfaces.
            20. Clear cache
            21. Lists the instrumented Java Virtual Machines (JVMs) on the target system.
            22. Report a snapshot of the current processes.
            23. Tell how long the system has been running(uptime).
            24. Check which program provide the command.
            25. Check the connectivity to IP
            26. Install Apache Web Server
            27. Start Apache Web Server
            28. Enable Apache Web Server
            29. Stop Apache Web Server
            30. Create a WebPage
            31. Stop Firewall
            32. Enable Firewall
            33. Get the current mode of SELinux
            34. modify the mode SELinux to permissive mode.
            35. modify the mode SELinux to enforcing mode.
            """)
            option = input("Select an option: ")

            if option == "1":
                os.system("date")
            elif option == "2":
                os.system("cal")
            elif option == "3":
                cmd = input("Enter command: ")
                manual = "man " + cmd
                os.system(manual)
            elif option == "4":
                os.system("ls")
            elif option == "5":
                dir_name = input("Enter directory name to create: ")
                new_dir = "mkdir " + dir_name
                os.system(new_dir)
                print("directory " + dir_name + " created")
            elif option == "6":
                dir_name = input("Enter directory name to be removed: ")
                rm_dir = "rmdir " + dir_name
                os.system(rm_dir)
                print("directory " + dir_name + " removed")
            elif option == "7":
                dir_path = input("Enter directory name or path: ")
                cd_dir = "cd " + dir_path
                os.system(cd_dir)
            elif option== "8":
                os.system("cd")
            elif option == "9":
                file_name = input("Enter file name to be created: ")
                new_file = "touch " + file_name
                os.system(new_file)
                print("file " + file_name + " created")
            elif option == "10":
                file_name = input("Enter file name to be created: ")
                new_file = "vim " + file_name
                os.system(new_file)
            elif option == "11":
                user_name = input("Enter new user name: ")
                new_user = "useradd " + user_name
                os.system(new_user)
                print("user " + user_name + " created")
            elif option == "12":
                user_name = input("Enter user name: ")
                new_passwd = "passwd " + user_name
                os.system(new_passwd)
            elif option == "13":
                os.system("cat /etc/passwd/")
            elif option == "14":
                yum_conf()
            elif option == "15":
                os.system("yum repolist")
            elif option == "16":
                os.system("lscpu")
            elif option == "17":
                os.system("free -m")
            elif option == "18":
                os.system("df -h")
            elif option == "19":
                os.system("ifconfig")
            elif option == "20":
                os.system("echo 3 > /proc/sys/vm/drop_caches")
            elif option == "21":
                os.system("jps")
            elif option == "22":
                os.system("ps -aux")
            elif option == "23":
                os.system("uptime")
            elif option == "24":
                cmd_name = input("Enter command to search: ")
                prog_name = "yum whatprovides " + cmd_name
                os.system(prog_name)
            elif option == "25":
                ip = input("Enter the IP to check connectivity: ")
                ping_ip = "ping -c 5 " + ip
                os.system(ping_ip)
            elif option == "26":
                os.system("yum install httpd")
            elif option == "27":
                os.system("systemctl start httpd")
            elif option == "28":
                os.system("systemctl enable httpd")
            elif option == "29":
                os.system("systemctl stop httpd")
            elif option == "30":
                web_test()
            elif option == "31":
                os.system("systemctl stop firewalld")
            elif option == "32":
                os.system("systemctl enable firewalld")
            elif option == "33":
                os.system("getenforce")
            elif option == "34":
                os.system("setenforce 0")
            elif option == "35":
                os.system("setenforce 1")
            elif option == "0":
                break
            else:
                os.system("tput setaf 1")
                print("ERROR: Select a valid option")
                os.system("tput setaf 7")
                print("")
            time.sleep(2)
            input("Press enter to continue")

    
    elif option == "2":
        while True:
            print("Hadoop Menu:")
            print("-----------")
            print("""
            0. Back to previous menu
            1. Check Hadoop version
            2. Format the DFS filesystem
            3. Start DFS Namenode 
            4. Stop DFS Namenode 
            5. Start DFS Datanode
            6. Stop DFS Datanode
            7. DFS admin client report
            8. Show a generic filesystem user client
            9. Upload a file to filesystem
            10. Remove a file from filesystem
            11. View the content of any file in hdfs
            12. Upload file with defined block size
            13. Create an empty file in hdfs
            """)
            option = input("select an option: ")
            if option == "1":
                os.system("hadoop version")
            elif option == "2":
                os.system("hadoop namenode -format")
            elif option == "3":
                os.system("hadoop-daemon.sh start namenode")
            elif option == "4":
                os.system("hadoop-daemon.sh stop namenode")
            elif option == "5":
                os.system("hadoop-daemon.sh start datanode")
            elif option == "6":
                os.system("hadoop-daemon.sh stop datanode")
            elif option == "7":
                os.system("hadoop dfsadmin -report")
            elif option == "8":
                os.system("hadoop fs -ls /")
            elif option == "9":
                file_path = input("Enter file path: ")
                file_source = "hadoop fs -put " + file_path
                file_dest = input("Enter file destination: ")
                file_upload = file_source + file_dest
                os.system(file_upload)
            elif option == "10":
                file_name = input("Enter file name to be deleted: ")
                file_del = "hadoop fs -rm " + file_name
                os.system(file_del)
            elif option == "11":
                file_name = input("Enter file to read: ")
                file_read = "hadoop fs -cat " + file_name
                os.system(file_read)
            elif option == "12":
                block_size = input("Enter bolck size (in bytes): ")
                blockSize == "hadoop fs _Ddfs.block.size=" + block_size
                file_path = input("Enter file Path: ")
                file_source = blockSize + " -put " + file_path + " "
                file_dest = input("Enter destination of file to be uploaded: ")
                file_upload = file_source + file_dest
                os.system(file_upload)
            elif option == "13":
                file_name = input("Enter  file name to be created: ")
                file_new = "hadoop fs -touchz / " + file_name
                os.system(file_new)
            elif option == "0":
                break
            else:
                os.system("tput setaf 1")
                print("ERROR: Select a valid option")
                os.system("tput setaf 7")
                print("")
            time.sleep(2)
            input("Press enter to continue")

    elif option == "3":
        while True:
            print("""
            AWS
            -----
            1. Install AWS cli
            2. Check version of AWS cli
            3. configure AWS
            4. Create a Key pair
            5. Create a Security Group
            6. Launch an EC2 instance
            7. Create EBS
            8. Attach EBS
            9. create S3 Bucket
            10. Store file in s3 Bucket
            """)
            option = input("Select an option: ")
            if option == "1":
                print("not supported")
            elif option == "2":
                os.system("aws --version")
            elif option == "3":
                os.system("aws configure")
            elif option == "4":
                key_name = input("Enter key name: ")
                os.system("aws ec2 create-key-pair --key-name {key_name}")
            elif option == "5":
                group_name = input("Enter group name: ")
                description = input("Enter description of security group: ")
                os.system('aws ec2 create-security-group --group-name {group_name} --description "{description}" ')
            elif option == "6":
                ami = input("Enter Amazon Machine Image ID: ")
                instance_type = input("Enter instance type: ")
                count = input("Enter number of instances to launch: ")
                subnet_id = input("Enter subnet id, where you want to launch: ")
                key_name = input("Enter a key pair value: ")
                security_group = input("Enter security group name: ")
                os.system("aws ec2 run-intances --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} --security-group-ids {security_group}")
            elif option == "7":
                zone = input("Enter availability zone: ")
                size = input("Enter the size of EBS: ")
                os.system("aws ec2 create-volume --availability-zone {zone} --no-encrypted --size {size}")
            elif option == "8":
                instance_id = input("Enter Instance ID: ")
                volume_id = input("Enter Volume ID: ")
                os.system("aws ec2 attach-volume --instance-id {instance_id} --volume-id {volume_id} --device xvdh")
            elif option == "9":
                bucket_name = input("Enter unique bucket name: ")
                region = input("Enter the region: ")
                os.system("aws s3api create-bucket --bucket {bucket_name} --region {region} --create-bucket-configuration LocationConstraint={reion}")
            elif option == "10":
                bucket = input("Enter Bucket name: ")
                file_object = input("Enter path of the object with name: ")
                name_dir = input("Enter name of object to be saved on bucket: ")
                os.system("aws s3api put-object --bucket {bucket} --key {name_dir} --body \"{file_object}\"")
            elif option == "0":
                break
            else:
                os.system("tput setaf 1")
                print("ERROR: Select a valid option")
                os.system("tput setaf 7")
                print("")
            time.sleep(2)
            input("Press enter to continue")
        
    elif option == "4":
        while True:
            print("""
            Docker
            ------
            0. Back to previous menu
            1. Check Docker version
            2. Create a container
            3. pull image from dockerhub
            4. List running docker containers
            5. List all docker containers
            6. List all images
            7. Start a docker container
            8. Stop a docker container
            9. Delete a docker container
            10. Stop all docker containers
            11. Delete all docker containers
            """)
            option = input("Select an option: ")

            if option == "1":
                os.system("docker version")
            elif option == "2":
                image_name = input("Enter image name: ")
                version = input("Enter image version: ")
                container = "docker run -it " + image_name + ":" + version
                os.system(container)
            elif option == "3":
                image_name = input("Enter image name: ")
                version = input("Enter image version: ")
                container = "docker pull " + image_name + ":" + version
                os.system(container)
            elif option == "4":
                os.system("docker ps")
            elif option == "5":
                os.system("docker ps -a")
            elif option == "6":
                os.system("docker images")
            elif option == "7":
                container_name = input("Enter container name: ")
                container = "docker container start " + container_name
                os.system(container)
            elif option == "8":
                container_name = input("Enter container name: ")
                container = "docker container stop " + container_name
                os.system(container)
            elif option == "9":
                container_name = input("Enter container name: ")
                container = "docker container rm " + container_name
                os.system(container)
            elif option == "10":
                os.system("docker container rm $(docker container ls -aq)")
            elif option == "11":
                os.sytem("docker container stop $(docker container ls -aq)&& docker system prune -af --volumes")
            elif option == "0":
                break
            else:
                os.system("tput setaf 1")
                print("ERROR: Select a valid option")
                os.system("tput setaf 7")
                print("")
            time.sleep(2)
            input("Press enter to continue")

    else:
        print("ERROR: Select a valid option")

