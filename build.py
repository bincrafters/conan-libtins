from conan.packager import ConanMultiPackager, os


if __name__ == "__main__":
    os.environ["CONAN_UPLOAD_ONLY_WHEN_STABLE"]="True"
    builder = ConanMultiPackager(
        args="--build missing",
        reference="libtins/3.5",
        stable_branch_pattern="stable*",
        stable_channel="stable",
        upload="https://api.bintray.com/conan/bincrafters/public-conan",
        remotes="https://api.bintray.com/conan/conan-community/conan")
    builder.add_common_builds()
    builder.run()
