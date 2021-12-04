node {
    try{
      def repoInformation = checkout scm
      def GIT_COMMIT_HASH = repoInformation.GIT_COMMIT


      def parallelTestConfiguration = [
        [
        '[test 1]': 'bikroy-python-selenium/tests/test_1',
        '[test 2_3]': 'bikroy-python-selenium/tests/test_2_3',
        '[test 4]': 'bikroy-python-selenium/tests/test_4',
        '[test 5]': 'bikroy-python-selenium/tests/test_5',
        '[test 6]': 'bikroy-python-selenium/tests/test_6',
        '[test 7]': 'bikroy-python-selenium/tests/test_7',
        '[test 8]': 'bikroy-python-selenium/tests/test_8',
        '[test 9]': 'bikroy-python-selenium/tests/test_9',
        '[test 10]': 'bikroy-python-selenium/tests/test_10',
        '[test 11]': 'bikroy-python-selenium/tests/test_11',
        '[test 12]': 'bikroy-python-selenium/tests/test_12',


        ]
      ]

      def stepList = prepareBuildStages(parallelTestConfiguration)

      for (def groupOfSteps in stepList) {
        parallel groupOfSteps
      }

    } catch(error) {
      echo "The following error occurred: ${error}"
      throw error
    } finally {
      allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'target/allure-results']]
      ])
    }
}


def prepareBuildStages(List<Map<String,String>> parallelTestConfiguration) {
  def stepList = []

  println('Preparing builds...')

  for (def parallelConfig in  parallelTestConfiguration) {
    def parallelSteps = prepareParallelSteps(parallelConfig)
    stepList.add(parallelSteps)
  }

  println(stepList)
  println('Finished preparing builds!')

  return stepList
}


def prepareParallelSteps(Map<String, String> parallelStepsConfig) {
  def parallelSteps = [:]
  for (def key in parallelStepsConfig.keySet()) {
    parallelSteps.put(key, prepareOneBuildStage(key, parallelStepsConfig[key]))
  }
  return parallelSteps
}

def prepareOneBuildStage(String name, String file) {
  return {
    stage("Test: ${name}") {
      println("Test: ${name}")
        withCredentials([
            string(credentialsId: 'pwd_jz_su', variable: 'pwd_jz_su'),
            string(credentialsId: 'db_pwd_aws', variable: 'db_pwd_aws'),
            string(credentialsId: 'selenium_grid_16ram', variable: 'selenium_grid_16ram'),
            ]) {
              // Tests go here
              sh """
                python3 -m pytest ${file}.py --alluredir=${WORKSPACE}/allure-results
              """
          }
    }
  }
}