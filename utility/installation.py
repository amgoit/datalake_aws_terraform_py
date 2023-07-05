import os

# Installation document Terraform
def print_check():
  print("Installation has been done successfully...")
  #os.system('yum install wget')

def install_terraform():
        os.system('sudo yum install -y yum-utils')
        os.system('sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo')
        os.system('sudo yum -y install terraform')


# Installation document AWS CLI - https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html
def install_aws_cli():
        os.system('sudo yum install -y wget')
        os.system('curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.312.zip" -o "awscli-bundle.zip" ;unzip awscli-bundle.zip ;sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws')
