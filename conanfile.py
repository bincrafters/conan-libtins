from conans import ConanFile, CMake, tools
import os

class LibtinsConan(ConanFile):
    name = "libtins"
    version = "4.1"
    author = "mfontanini"
    description = "High-level, multiplatform C++ network packet sniffing and crafting library"
    topics = ("conan", "libpcap", "winpcap", "pcap", "networking", "packets")
    license = "MIT"
    url = "https://github.com/bincrafters/conan-libtins"
    homepage = "https://github.com/mfontanini/libtins"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "BSD-2-Clause"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "enable_pcap": [True, False],
        "enable_cxx11": [True, False],
        "enable_dot11": [True, False],
        "enable_wpa2": [True, False],
        "enable_tcpip": [True, False],
        "enable_ack_tracker": [True, False],
        "enable_tcp_stream_custom_data": [True, False]
    }
    default_options = {
        "shared": True, 
        "enable_pcap": True, 
        "enable_cxx11": True,
        "enable_dot11": True,
        "enable_wpa2": True,
        "enable_tcpip": True,
        "enable_ack_tracker": True,
        "enable_tcp_stream_custom_data": True,
    }
    
    _source_subfolder = "source_subfolder"
    
    def requirements(self):
        if self.options.enable_pcap:
            if self.settings.os == "Windows":
                self.requires.add("winpcap/4.1.3@bincrafters/stable")
            else:
                self.requires.add("libpcap/1.8.1@uilianries/stable")
        if self.options.enable_wpa2:
            self.requires.add("OpenSSL/1.0.2l@conan/stable")
        if self.options.enable_ack_tracker or self.options.enable_tcp_stream_custom_data:
            self.requires.add("boost_icl/1.69.0@bincrafters/stable")
            self.requires.add("boost_any/1.69.0@bincrafters/stable")
            
    def source(self):
        sha256sum = "81a0ae1e04499b25984b2833579d33c4a78ff4513e9a14176c574e855163f7a5"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256sum)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
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
        cmake.configure(source_dir=self._source_subfolder)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        # self.copy("LICENSE", dst=".", keep_path=False)
        # self.copy("*.h", dst="include", src=os.path.join(self.name, "include"))
        # self.copy("*.dll", dst="bin", keep_path=False)
        # self.copy("*.so*", dst="lib", keep_path=False)
        # self.copy("*.dylib", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)
        # self.copy("*.lib", dst="lib", keep_path=False)
        
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()
            
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
