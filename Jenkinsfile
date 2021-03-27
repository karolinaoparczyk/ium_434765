pipeline {
    agent any
    stages {
        stage('Clone repo') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://git.wmi.amu.edu.pl/s434765/ium_434765']]])
                sh get_data_simple.sh
                archiveArtifacts data_dev
                archiveArtifacts data_shuf
                archiveArtifacts data_test
                archiveArtifacts data_train
            }
        }
    }
}