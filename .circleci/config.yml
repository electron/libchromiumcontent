version: 2.1

jobs:
  hello-job:
    docker:
      - image: cimg/node:17.2.0 # the primary container, where your job's commands are run
        auth:
          username: mydockerhub-user
          password: $DOCKERHUB_PASSWORD  # context / project UI env-var reference
    steps:
      - checkout # check out the code in the project directory
      - run: echo "hello world" # run the `echo` command

workflows:
  my-workflow:
    jobs:
      - hello-job
