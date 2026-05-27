pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER = 'C:\\Users\\gayes\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
    }

    stages {

        stage('Build') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
                bat '"%DOCKER%" build -t wellness-app .'
            }
        }

        stage('Test') {
            steps {
                bat '"%PYTHON%" -m pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                bat '"%PYTHON%" -m pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat '"%PYTHON%" -m bandit -r .'
            }
        }

        stage('Deploy') {
            steps {
                bat '"%DOCKER%" run -d -p 5000:5000 wellness-app'
            }
        }

        stage('Monitoring') {
            steps {
                bat 'curl http://localhost:5000/health'
            }
        }
    }
}