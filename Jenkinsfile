pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t wellness-app .'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pylint app.py'
            }
        }

        stage('Security Scan') {
            steps {
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m bandit -r .'
            }
        }

        stage('Deploy') {
            steps {
                bat '"C:\\Users\\gayes\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d -p 5000:5000 wellness-app'
            }
        }

        stage('Monitoring') {
            steps {
                bat 'powershell -Command "(Invoke-WebRequest http://localhost:5000/health).StatusCode"'
            }
        }
    }
}