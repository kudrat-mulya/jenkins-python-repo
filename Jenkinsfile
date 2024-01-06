pipeline {
    agent {
        docker {
            image 'python:3.9-bullseye' 
            args '-p 3000:3000' 
        }
    }
    stages {
        stage('Cek versi python') { 
            steps {
                sh 'python3 --version'
            }
        }
        stage('Run script') {
            steps {
                sh 'python3 python_script.py'
            }
        }
        // stage('Deploy') {
            // steps {
                // sh './jenkins/scripts/deliver.sh'
                // input message: 'sudah selesai menggunakan react app? (klik "proceed" untuk mengakhiri)'
                // sh './jenkins/scripts/kill.sh'
            // }
        // }
    }
} 
