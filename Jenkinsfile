node {
    try {
        stage('Build') {
            checkout scm
            sh 'python setup.py sdist upload -r pypi'
        }
    } catch (e) {
        currentBuild.result = "FAILED"
        throw e
    } finally {
        mail body: "See ${currentBuild.absoluteUrl} for details", subject: "Hexahub build ${currentBuild.result}", to: 'xobb@citylance.biz'
    }
}