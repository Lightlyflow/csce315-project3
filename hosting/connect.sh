# Make sure your WSL is configured to allow for metadata changes on the mounted drive
# https://stackoverflow.com/questions/46610256/chmod-wsl-bash-doesnt-work#answer-50856772

P_KEY="LightsailDefaultKey-us-east-2.pem"

chmod 600 "$P_KEY"
ssh -i "$P_KEY" ubuntu@3.138.69.24