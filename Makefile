PKG_NAME := shaderc
URL = https://github.com/google/shaderc/archive/refs/tags/v2024.0.tar.gz
ARCHIVES = https://github.com/KhronosGroup/SPIRV-Tools/archive/vulkan-sdk-1.3.275.0/SPIRV-Tools-1.3.275.0.tar.gz third_party/spirv-tools https://github.com/KhronosGroup/SPIRV-Headers/archive/sdk-1.3.261.0/SPIRV-Headers-1.3.261.0.tar.gz third_party/spirv-headers https://github.com/KhronosGroup/glslang/archive/14.1.0/glslang-14.1.0.tar.gz third_party/glslang

include ../common/Makefile.common
