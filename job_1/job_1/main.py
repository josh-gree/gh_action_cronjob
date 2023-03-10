from prefect import flow, task


@task
def say_hello():
    print("Hello world")


@flow
def main():
    say_hello()


if __name__ == "__main__":
    main()
