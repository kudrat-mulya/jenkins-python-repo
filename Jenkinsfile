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
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }
        stage('Upgrade Pip') {
            steps {
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }
        stage('Adjust Permissions') {
            steps {
                def home = sh(script: 'echo $HOME', returnStdout: true).trim()
                sh "chmod -R 755 $home/.local"
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt --target=venv/lib/python3.9/site-packages'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
        stage('Cek versi python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Run script') {
            steps {
                sh 'python3 python_script2.py'
            }
        }
    }
}
