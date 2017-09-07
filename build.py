from conan.packager import ConanMultiPackager, os


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing", username=os.getenv("CONAN_USERNAME"), channel=os.getenv("CONAN_CHANNEL"))
    builder.add_common_builds()
    builder.run()
