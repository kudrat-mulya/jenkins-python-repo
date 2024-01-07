pipeline {
    agent {
        docker {
            image 'node:16-buster-slim'
            args '-p 3000:3000'
        }
    }
    
    stages {
        stage('Build') { 
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh './jenkins/scripts/test.sh'
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
