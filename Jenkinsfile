pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'docker build -t wellness-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                bat 'python -m pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'python -m bandit -r .'
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