import os


def create_agency():
  agency_name = input(f'Please enter the agency name (Note don\'t use symbol): ')
  os.system(f"mkdir -p agencies/{agency_name.strip()}")
#  os.system(f"cp main.tf variable.tf agencies/{agency_name.strip()};cd agencies/{agency_name.strip()}; terraform init;export TF_VAR_username={agency_name.strip()};terraform apply --auto-approve")
  os.system(f"cp main.tf variable.tf agencies/{agency_name.strip()};cd agencies/{agency_name.strip()}; terraform init;export TF_VAR_username={agency_name.strip()};terraform apply --auto-approve")
  os.system(f"cat 'create|Agency|{agency_name.strip()}' >> ../../HEAD")

