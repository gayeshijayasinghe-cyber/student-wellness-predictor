pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'docker build -t wellness-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                bat 'pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'bandit -r .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 wellness-app'
            }
        }

        stage('Monitoring') {
            steps {
                bat 'curl http://localhost:5000/health'
            }
        }
    }
}