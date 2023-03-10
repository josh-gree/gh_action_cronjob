import os


def main():
    print("Hello World!")
    print(os.environ.get("SOME_ENV_VAR", "Not Found!"))
    print(os.environ.get("SOME_SECRET_ENV_VAR", "Not Found!"))


if __name__ == "__main__":
    main()
