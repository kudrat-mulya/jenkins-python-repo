pipeline {
    agent any
    
    environment {
        PATH = "/usr/local/bin:$PATH"
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
                    echo "Installing required packages..."
                    sh 'apt-get update && apt-get install -y python3 python3-pip'
                    echo "Upgrading pip..."
                    sh 'pip3 install --upgrade pip'
                    echo "Building..."
                    sh 'pip3 install -r requirements.txt --user'
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
