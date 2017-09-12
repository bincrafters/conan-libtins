from conans import ConanFile, CMake, tools, os

class LibtinsConan(ConanFile):
    name = "libtins"
    version = "3.5"
    author = "mfontanini"
    description = "High-level, multiplatform C++ network packet sniffing and crafting library"
    license = "https://github.com/mfontanini/libtins/blob/master/LICENSE"
    url = "https://github.com/bincrafters/conan-libtins"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "enable_pcap": [True, False],
        "enable_cxx11": [True, False],
        "enable_dot11": [True, False],
        "enable_wpa2": [True, False],
        "enable_tcpip": [True, False],
        "enable_ack_tracker": [True, False],
        "win_capture_lib": ["winpcap", "npcap"],
        "enable_tcp_stream_custom_data": [True, False]
    }
    default_options = "shared=True", "enable_pcap=True", "enable_cxx11=True", "enable_dot11=True", "enable_wpa2=True", "enable_tcpip=True", "enable_ack_tracker=True", "enable_tcp_stream_custom_data=True", "win_capture_lib=npcap"
    generators = "cmake"

    def requirements(self):
        if self.options.enable_pcap:
            if self.settings.os == "Windows":
                if self.options.win_capture_lib == "npcap":
                    self.requires.add("WinPcap/4.1.2@RoliSoft/stable")
                else:
                    self.requires.add("npcap/0.93@bincrafters/testing")
            else:
                self.requires.add("libpcap/1.8.1@uilianries/stable")
        if self.options.enable_wpa2:
            self.requires.add("OpenSSL/1.0.2l@conan/stable")
        if self.options.enable_ack_tracker or self.options.enable_tcp_stream_custom_data:
            self.requires.add("Boost/1.64.0@conan/stable")

    def source(self):
        source_url =  "https://github.com/mfontanini/libtins"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, archive_name))
        os.rename(self.name + "-" + self.version  , self.name)

    def build(self):
        conan_magic_lines = """PROJECT(libtins)
    INCLUDE(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    CONAN_BASIC_SETUP()"""
        tools.replace_in_file(os.path.join(self.name, "CMakeLists.txt"), "PROJECT(libtins)", conan_magic_lines)
        cmake = CMake(self)
        cmake.definitions["LIBTINS_BUILD_SHARED"] = self.options.shared
        cmake.definitions["LIBTINS_ENABLE_PCAP"] = self.options.enable_pcap
        cmake.definitions["LIBTINS_ENABLE_CXX11"] = self.options.enable_cxx11
        cmake.definitions["LIBTINS_ENABLE_DOT11"] = self.options.enable_dot11
        cmake.definitions["LIBTINS_ENABLE_WPA2"] = self.options.enable_wpa2
        cmake.definitions["LIBTINS_ENABLE_TCPIP"] = self.options.enable_tcpip
        cmake.definitions["LIBTINS_ENABLE_ACK_TRACKER"] = self.options.enable_ack_tracker
        cmake.definitions["LIBTINS_ENABLE_TCP_STREAM_CUSTOM_DATA"] = self.options.enable_tcp_stream_custom_data
        cmake.definitions["LIBTINS_BUILD_TESTS"] = False
        cmake.definitions["LIBTINS_BUILD_EXAMPLES"] = False
        cmake.configure(source_dir=self.name)
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst=".", keep_path=False)
        self.copy("*.h", dst="include", src=os.path.join("libtins", "include"))
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
            
    def package_info(self):
        self.cpp_info.libs = self.collect_libs()
