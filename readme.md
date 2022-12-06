# Hello CodeSpace


account plan	Storage per month	Core hours per month
GitHub Free for personal accounts	15 GB-month	120
GitHub Pro	20 GB-month	180

Push to docker hub
- docker tag ${Image Name} DockerHub帳號/Image Name
- docker login
- docker push DockerHub帳號/Image Name

get-aws-ssh-ip-script:
	aws ec2 describe-instances --filters 'Name=tag:Name,Values=ssh_b' --query 'Reservations[].Instances[].PublicIpAddress'

make-python-env:
	virtualenv playground

active-python-env:
	source playground/bin/activate