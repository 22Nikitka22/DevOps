pipeline {
    agent any

    environment {
        // Укажите необходимые переменные окружения
        ALLURE_VERSION = '2.13.9'
        SONAR_SCANNER_HOME = '/opt/sonar-scanner'
        DOCKER_IMAGE_NAME = 'nikitka22/myapp:2.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                // Клонирование репозитория
                git url: 'https://github.com/22Nikitka22/DevOps-2024.git', branch: 'hometask-4'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Установка зависимостей
                    sh 'apt-get install -y python3-psycopg2'
                    sh 'python myapp/app.py build'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск автотестов
                    sh 'apt-get install -y python3-pytest python3-pip'
                    sh 'pip3 install pytest-allure'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Установка Allure
                    sh "curl -o allure.zip -L 'https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}-linux.zip'"
                    sh 'unzip allure.zip -d /opt/allure'
                    sh 'rm allure.zip'

                    // Генерация отчета
                    sh '/opt/allure/bin/allure generate allure-results --clean -o allure-report'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                // Публикация отчета в Jenkins
                allure([
                    results: [[path: 'allure-results']],
                    report: 'allure-report'
                ])
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Запуск анализа SonarQube
                    withSonarQubeEnv('SonarQube') { // Убедитесь, что вы настроили SonarQube в Jenkins
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Сборка Docker-образа
                    sh "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }
    }

    post {
        always {
            // Удаление временных файлов
            cleanWs()
        }
    }
}