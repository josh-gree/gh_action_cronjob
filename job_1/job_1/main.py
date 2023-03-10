from prefect import flow


@flow
def main():
    print("Hello world")


if __name__ == "__main__":
    main()
