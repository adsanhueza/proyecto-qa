pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\certi\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }

    stages {
        stage('Descargar código') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno') {
            steps {
                bat '"%PYTHON%" -m venv venv'
                bat 'venv\\Scripts\\python -m pip install -r requirements.txt'
                bat 'venv\\Scripts\\python -m playwright install chromium'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                bat 'venv\\Scripts\\python -m pytest --junitxml=resultados.xml --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit testResults: 'resultados.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}