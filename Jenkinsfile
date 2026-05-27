pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\gayes\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER = 'C:\\Users\\gayes\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        POWERSHELL = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
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

                bat '''
                for /F %%i in ('"%DOCKER%" ps -q') do "%DOCKER%" stop %%i
                '''

                bat '''
                for /F %%i in ('"%DOCKER%" ps -aq') do "%DOCKER%" rm %%i
                '''

                bat '"%DOCKER%" run -d --name wellness-container -p 5000:5000 wellness-app'

                bat '"%DOCKER%" logs wellness-container'
            }
        }

        stage('Monitoring') {
            steps {

            bat '"%DOCKER%" logs wellness-container'

            bat '"%POWERSHELL%" -Command "Start-Sleep -Seconds 20"'

            bat '"%POWERSHELL%" -Command "try { (Invoke-WebRequest http://localhost:5000/health).StatusCode } catch { Write-Host $_; exit 1 }"'
            }
        }
    }
}