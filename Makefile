PKG_NAME := shaderc
URL = https://github.com/google/shaderc/archive/v2024.3/shaderc-2024.3.tar.gz
ARCHIVES = https://github.com/KhronosGroup/SPIRV-Tools/archive/vulkan-sdk-1.3.290.0/SPIRV-Tools-1.3.290.0.tar.gz third_party/spirv-tools https://github.com/KhronosGroup/SPIRV-Headers/archive/vulkan-sdk-1.3.290.0/SPIRV-Headers-1.3.290.0.tar.gz third_party/spirv-headers  https://github.com/KhronosGroup/glslang/archive/15.0.0/glslang-15.0.0.tar.gz third_party/glslang

include ../common/Makefile.common
