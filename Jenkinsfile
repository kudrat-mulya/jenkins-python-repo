pipeline {
    agent {
        docker {
            image 'python:3.9-bullseye'
            args '-p 3000:3000'
        }
    }
    
    stages {
        stage('Prepare Environment') {
            steps {
                echo "Current user: ${env.USER}"
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'chmod -R 755 /.local'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Current user: ${env.USER}"
                sh 'ls -ld /.cache'
                sh 'pip install --upgrade --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Current user: ${env.USER}"
                sh 'python3 -m unittest discover'
            }
        }

        stage('Run Script') {
            steps {
                echo "Current user: ${env.USER}"
                sh 'python3 python_script2.py'
            }
        }
    }
}
