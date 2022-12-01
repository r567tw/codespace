sync-docker-compose.yml:
	cp docker-compose.yml ../docker-compose.yml

get-aws-ssh-ip-script:
	aws ec2 describe-instances --filters 'Name=tag:Name,Values=ssh_b' --query 'Reservations[].Instances[].PublicIpAddress'

make-python-env:
	virtualenv playground

active-python-env:
	source playground/bin/activate

workspace-folders:
	./make_workspace_folder.sh
