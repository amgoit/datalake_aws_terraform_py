import os

# Installation document Terraform

def agency_delete():
  print("Below the Agency to delete the Agency\n")
  os.system("ls -lhrt | awk '{print $NF }'")
  agency_name = input(f'Please enter the agency name (Note don\'t use symbol): ')
  
  os.system(f"cd agencies/{agency_name.strip()}; terraform destroy -target aws_iam_user.lake_user --auto-approve")
#  os.system(f"cp main.tf variable.tf agencies/{agency_name.strip()};cd agencies/{agency_name.strip()}; terraform init;export TF_VAR_username={agency_name.strip()};terraform apply --auto-approve")
#  os.system(f"cp main.tf variable.tf agencies/{agency_name.strip()};cd agencies/{agency_name.strip()}; terraform init;export TF_VAR_username={agency_name.strip()};terraform apply --auto-approve")
  os.system(f"cat 'delete|Agency|{agency_name.strip()}' >> ../../HEAD")

