from conans import ConanFile, CMake, tools
import os

class LibtinsConan(ConanFile):
    name = "libtins"
    version = "4.2"
    author = "mfontanini"
    description = "High-level, multiplatform C++ network packet sniffing and crafting library"
    topics = ("conan", "libpcap", "winpcap", "pcap", "networking", "packets")
    license = "MIT"
    url = "https://github.com/bincrafters/conan-libtins"
    homepage = "https://github.com/mfontanini/libtins"
    license = "BSD-2-Clause"
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
                self.requires("winpcap/4.1.3@bincrafters/stable")
            else:
                self.requires("libpcap/1.9.1")
        if self.options.enable_wpa2:
            self.requires("openssl/1.0.2u")
        if self.options.enable_ack_tracker or self.options.enable_tcp_stream_custom_data:
            self.requires("boost_icl/1.69.0@bincrafters/stable")
            self.requires("boost_any/1.69.0@bincrafters/stable")
            
    def source(self):
        sha256sum = "a9fed73e13f06b06a4857d342bb30815fa8c359d00bd69547e567eecbbb4c3a1"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version), sha256=sha256sum)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
        tools.replace_in_file(
            "{0}/src/CMakeLists.txt".format(self._source_subfolder), 
            "    EXPORT libtinsTargets\n",
            "    EXPORT libtinsTargets\n" +             "    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}\n")

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
        cmake.configure()
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder, keep_path=False)
        cmake = self._configure_cmake()
        cmake.install()
            
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if not self.options.shared:
            self.cpp_info.defines.append("TINS_STATIC")
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("Iphlpapi")
