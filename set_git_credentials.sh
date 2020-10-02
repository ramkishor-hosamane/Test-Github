echo "Github Configuration"
echo "--------------------"
sleep 1
echo
read -p "Enter your github username : " username
read -s -p "Enter your github password : " password
echo -p "$pass" | sed 's/./*/g'
read -p "Enter github repository username : " git_repo_username
read -p "Enter github repository name : " repository


git remote set-url origin https://$username:$password@github.com/$git_repo_username/$repository.git
echo "Done!!!!"
