from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing", username="bincrafters")
    builder.add_common_builds()
    builder.run()
