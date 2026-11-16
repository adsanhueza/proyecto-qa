pipeline {
    agent any

    stages {
        stage('Descargar código') {
            steps {
                checkout scm
            }
        }

        stage('Preparar entorno') {
            steps {
                bat 'python -m venv venv'
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
            junit 'resultados.xml'
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}