from conan.packager import ConanMultiPackager, os


if __name__ == "__main__":
    builder = ConanMultiPackager(
        upload="https://api.bintray.com/conan/bincrafters/public-conan",
        remotes="https://api.bintray.com/conan/conan-community/conan")
    builder.add_common_builds()
    builder.run()
