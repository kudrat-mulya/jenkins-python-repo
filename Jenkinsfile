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
                sh 'pip install --upgrade pip'
                sh 'chown -R ${env.USER}:${env.USER} ~/.cache/pip'
                sh 'pip install --upgrade --user pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Current user: ${env.USER}"
                sh 'chown -R ${env.USER}:${env.USER} venv'
                sh 'pip install --user -r requirements.txt'
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

