pipeline {
    agent any
    stages {
        stage('SCM Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shivalikag17/devopsexam.git'
            }
        }
        stage('Docker image build') {
            steps {
                sh '/usr/bin/docker image build -t shivalika17/ditissimage .'
            }
        }
        stage('Docker login') {
            steps {
                sh 'echo dckr_pat_upZWFBxtIVqnMkB8ye5LnrBfY1g | /usr/bin/docker login -u shivalika17 --password-stdin'
          }
        }
        stage('Service create') {
            steps {
                sh '/usr/bin/docker container run -itd --name exam -p 4000:4000  shivalika17/ditissimage'
            }
        }
    }
}
