Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/jammy64"
    config.vm.synced_folder ".", "/app"
    config.ssh.forward_agent = true
    config.vm.provision "shell", inline: <<-SHELL
        # Update and install dependencies
        sudo apt update
        sudo apt install -y git curl unzip apt-transport-https gnupg lsb-release software-properties-common

        git config --global user.email "ramtin.kazemi@gmail.com"
        git config --global user.name "Ramtin Kazemi"

        # Install Pre-commit
        sudo apt install -y pre-commit
        pushd /app > /dev/null
        pre-commit install
        popd > /dev/null

        # Install Python 3
        sudo apt install -y python3 python3-pip
        echo 'alias python=python3' >> /home/vagrant/.bashrc
        echo 'alias py=python3' >> /home/vagrant/.bashrc

        # Install AWS CLI
        curl -o awscliv2.zip -SLf "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" 
        unzip awscliv2.zip
        sudo ./aws/install && rm -rf aws awscliv2.zip
        echo 'complete -C '/usr/local/bin/aws_completer' aws' >> /home/vagrant/.bashrc

        # Install CodeCommit credential helper
        git config --global credential.helper '!aws codecommit credential-helper $@'
        git config --global credential.UseHttpPath true

        # Install eksctl
        curl -o eksctl.tar.gz -SLf "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz"
        tar -xz -f eksctl.tar.gz -C /tmp        
        sudo mv /tmp/eksctl /usr/local/bin && rm eksctl.tar.gz
        
        # Install Terraform
        TERRAFORM_VERSION="1.6.6"
        curl -o terraform.zip -SLf https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
        unzip terraform.zip 
        mv terraform /usr/local/bin/ 
        rm terraform.zip 
        echo 'alias tf=terraform' >> /home/vagrant/.bashrc

        # Install tflint
        TFLINT_VERSION="0.50.0"
        curl -o tflint.zip -SLf https://github.com/terraform-linters/tflint/releases/download/v${TFLINT_VERSION}/tflint_linux_amd64.zip
        unzip tflint.zip 
        sudo mv tflint /usr/local/bin/ 
        tflint --version 
        rm tflint.zip

        # Install tfsec
        TFSEC_VERSION="1.28.4"
        curl -o tfsec -SLf https://github.com/aquasecurity/tfsec/releases/download/v${TFSEC_VERSION}/tfsec-linux-amd64
        chmod +x tfsec
        mv tfsec /usr/local/bin/
        tfsec --version

        # Install Terragrunt
        TERRAGRUNT_VERSION="0.54.11"
        curl -o terragrunt -SLf https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64
        chmod +x terragrunt
        sudo mv terragrunt /usr/local/bin/
        echo 'alias tg=terragrunt' >> /home/vagrant/.bashrc

        # Install kubectl
        KUBECTL_VERSION="1.28.0"
        curl -o kubectl -SLf "https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
        chmod +x ./kubectl
        sudo mv ./kubectl /usr/local/bin/kubectl
        kubectl completion  >> /home/vagrant/.bashrc
        echo 'alias k=kubectl' >> /home/vagrant/.bashrc

        # Install Helm
        HELM_VERSION="3.13.3"
        curl -o helm.tar.gz -SLf https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz
        tar -zxvf helm.tar.gz -C /tmp
        sudo mv /tmp/linux-amd64/helm /usr/local/bin/helm
        rm -rf helm.tar.gz 
        echo 'alias h=helm' >> /home/vagrant/.bashrc

        # Install Golang
        GO_VERSION="1.21.5"
        curl -o go.tar.gz -SLf https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz
        sudo tar -C /usr/local -xzf go.tar.gz
        echo 'export PATH=$PATH:/usr/local/go/bin' >> /home/vagrant/.bashrc
        echo 'export GOPATH=$HOME/go' >> /home/vagrant/.bashrc
        rm go.tar.gz

        echo \
        'function git_branch {
            if git rev-parse --git-dir > /dev/null 2>&1; then
              branch=$(git branch 2>/dev/null | grep "^*" | colrm 1 2)
              if [[ $(git status --porcelain 2>/dev/null| wc -l) -gt 0 ]]; then
                echo -e " \033[1;31m[$branch*]\033[0m"  # Bold Red color for uncommitted changes
              else
                echo -e " \033[1;32m[$branch]\033[0m"   # Bold Green color for clean state
              fi
            fi
          }'  >> /home/vagrant/.bashrc

        echo "export PS1='\\[\\033[1;32m\\]\\u@\\h\\[\\033[0m\\]:\\w\$(git_branch)\\[\\033[0;37m\\] '" >> /home/vagrant/.bashrc

        echo "alias gco='git checkout'" >> /home/vagrant/.bashrc
        echo "alias gcm='git commit -m'" >> /home/vagrant/.bashrc
        echo "alias gad='git add'" >> /home/vagrant/.bashrc
        echo "alias gpl='git pull'" >> /home/vagrant/.bashrc
        echo "alias gps='git push'" >> /home/vagrant/.bashrc
        echo 'cd /app' >> /home/vagrant/.bashrc

      SHELL
  end
  