pipeline {
    agent {
        docker {
            image 'node:16-buster-slim'
            args '-p 3000:3000'
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Fixing permissions..."
                    sh 'sudo apt-get update && sudo apt-get install -y sudo'
                    sh 'sudo chmod -R 777 /var/lib/apt/lists'
                    sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                    echo "Upgrading pip..."
                    sh 'sudo pip install --upgrade pip'
                    echo "Building..."
                    sh 'sudo pip install -r requirements.txt --user'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    sh 'python3 -m unittest discover'
                }
            }
        }

        stage('Check Python Version') {
            steps {
                script {
                    echo "Checking Python version..."
                    sh 'python3 --version'
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    echo "Running python_script2.py..."
                    sh 'python3 python_script2.py'
                }
            }
        }
    }
}
