from utility import installation,aws_configure,agency_create,delete_agency

num=1
task_num=[]

tasks=['Installing AWS CLI', 'AWS CLI Configuration', 'Installing Terraform', 'Create New Agency and Bucket', 'Delete Agency', 'Exit']

def task_nums(num,task_num):
  print("Please Enter the number for below task :-\n")
  for task in tasks:
    print(f"{num}.) {task}")
    if task == 'Exit':
      task_num.append(0)
    else:
      task_num.append(num)
    num=num+1
  user_input(task_num)



def task_details(value):
  if value == 1:
    #installation.print_check()
    installation.install_aws_cli()
    print("######################################################################################################################################")
    task_num=[]
    task_nums(num,task_num)
  elif value == 2:
    aws_configure.aws_configuration()
    print("######################################################################################################################################")
    task_num=[]
    task_nums(num,task_num)
  elif value == 3:
    installation.install_terraform()
    print("#####################################################################################################################################")
    task_num=[]
    task_nums(num,task_num)
  elif value == 4:
    agency_create.create_agency()
    print("#####################################################################################################################################")
    task_num=[]
    task_nums(num,task_num)
  elif value == 6:
    delete_agency.agency_delete()
    print("#####################################################################################################################################")
    task_num=[]
    task_nums(num,task_num)
  elif value == 0:
    exit()
  else:
    exit()



def user_input(task_num):
  while True:
    value = input(f'Please enter the Option {task_num} : ')
    try:
      value = int(value)
    except ValueError:
      print('Oops ...!!! You have entered an invalid number.')
      continue
    if 0 <= value < len(task_num):
      task_details(value)
    else:
      print('Oops ...!!! You have entered an invalid number.')


task_nums(num,task_num)

