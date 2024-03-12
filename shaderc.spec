#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
Name     : shaderc
Version  : 2024.0
Release  : 4
URL      : https://github.com/google/shaderc/archive/refs/tags/v2024.0.tar.gz
Source0  : https://github.com/google/shaderc/archive/refs/tags/v2024.0.tar.gz
Source1  : https://github.com/KhronosGroup/SPIRV-Headers/archive/sdk-1.3.261.0/SPIRV-Headers-1.3.261.0.tar.gz
Source2  : https://github.com/KhronosGroup/SPIRV-Tools/archive/vulkan-sdk-1.3.275.0/SPIRV-Tools-1.3.275.0.tar.gz
Source3  : https://github.com/KhronosGroup/glslang/archive/14.1.0/glslang-14.1.0.tar.gz
Summary  : Tools and libraries for Vulkan shader compilation
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause-Clear MIT
Requires: shaderc-bin = %{version}-%{release}
Requires: shaderc-lib = %{version}-%{release}
Requires: shaderc-license = %{version}-%{release}
Requires: SPIRV-Tools
BuildRequires : SPIRV-Cross
BuildRequires : SPIRV-Headers-dev
BuildRequires : SPIRV-Tools
BuildRequires : SPIRV-Tools-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : glslang
BuildRequires : glslang-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : mesa-dev
BuildRequires : pypi-numpy
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Shaderc
A collection of tools, libraries and tests for shader compilation.
At the moment it includes:

%package bin
Summary: bin components for the shaderc package.
Group: Binaries
Requires: shaderc-license = %{version}-%{release}

%description bin
bin components for the shaderc package.


%package dev
Summary: dev components for the shaderc package.
Group: Development
Requires: shaderc-lib = %{version}-%{release}
Requires: shaderc-bin = %{version}-%{release}
Provides: shaderc-devel = %{version}-%{release}
Requires: shaderc = %{version}-%{release}

%description dev
dev components for the shaderc package.


%package lib
Summary: lib components for the shaderc package.
Group: Libraries
Requires: shaderc-license = %{version}-%{release}

%description lib
lib components for the shaderc package.


%package license
Summary: license components for the shaderc package.
Group: Default

%description license
license components for the shaderc package.


%prep
%setup -q -n shaderc-2024.0
cd %{_builddir}
tar xf %{_sourcedir}/SPIRV-Tools-1.3.275.0.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/SPIRV-Headers-1.3.261.0.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/glslang-14.1.0.tar.gz
cd %{_builddir}/shaderc-2024.0
mkdir -p third_party/spirv-tools
cp -r %{_builddir}/SPIRV-Tools-vulkan-sdk-1.3.275.0/* %{_builddir}/shaderc-2024.0/third_party/spirv-tools
mkdir -p third_party/spirv-headers
cp -r %{_builddir}/SPIRV-Headers-sdk-1.3.261.0/* %{_builddir}/shaderc-2024.0/third_party/spirv-headers
mkdir -p third_party/glslang
cp -r %{_builddir}/glslang-14.1.0/* %{_builddir}/shaderc-2024.0/third_party/glslang

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710256595
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DSHADERC_ENABLE_TESTS=FALSE \
-DSHADERC_SKIP_TESTS=ON \
-DSKIP_SPIRV_TOOLS_INSTALL=ON \
-DSKIP_GLSLANG_INSTALL=ON
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710256595
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/shaderc
cp %{_builddir}/SPIRV-Headers-sdk-1.3.261.0/LICENSE %{buildroot}/usr/share/package-licenses/shaderc/9a84200f47e09abfbde1a6b25028460451b23d03 || :
cp %{_builddir}/SPIRV-Tools-vulkan-sdk-1.3.275.0/LICENSE %{buildroot}/usr/share/package-licenses/shaderc/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/SPIRV-Tools-vulkan-sdk-1.3.275.0/utils/vscode/src/lsp/LICENSE %{buildroot}/usr/share/package-licenses/shaderc/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/glslang-14.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/shaderc/f77668fa8c7bb3dc2788af730150c401bd723fed || :
cp %{_builddir}/shaderc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/shaderc/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/shaderc-%{version}/third_party/LICENSE.glslang %{buildroot}/usr/share/package-licenses/shaderc/cdea109780799ce618a98a53a52efbae6afb8247 || :
cp %{_builddir}/shaderc-%{version}/third_party/LICENSE.spirv-tools %{buildroot}/usr/share/package-licenses/shaderc/f67a567c3c0f82d745f3f273bf1cadd6b1edcad4 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/spirv-as
rm -f %{buildroot}*/usr/bin/spirv-cfg
rm -f %{buildroot}*/usr/bin/spirv-dis
rm -f %{buildroot}*/usr/bin/spirv-lesspipe.sh
rm -f %{buildroot}*/usr/bin/spirv-link
rm -f %{buildroot}*/usr/bin/spirv-lint
rm -f %{buildroot}*/usr/bin/spirv-objdump
rm -f %{buildroot}*/usr/bin/spirv-opt
rm -f %{buildroot}*/usr/bin/spirv-reduce
rm -f %{buildroot}*/usr/bin/spirv-val
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-diff/SPIRV-Tools-diffConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-diff/SPIRV-Tools-diffTargets-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-diff/SPIRV-Tools-diffTargets.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkTargets-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-link/SPIRV-Tools-linkTargets.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-lint/SPIRV-Tools-lintConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-lint/SPIRV-Tools-lintTargets-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-lint/SPIRV-Tools-lintTargets.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optTargets-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-opt/SPIRV-Tools-optTargets.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceTarget-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-reduce/SPIRV-Tools-reduceTarget.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-tools/SPIRV-Tools-toolsConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-tools/SPIRV-Tools-toolsTargets-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools-tools/SPIRV-Tools-toolsTargets.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsConfig.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsTarget-relwithdebinfo.cmake
rm -f %{buildroot}*/usr/lib64/cmake/SPIRV-Tools/SPIRV-ToolsTarget.cmake
rm -f %{buildroot}*/usr/lib64/libSPIRV-Tools-shared.so
rm -f %{buildroot}*/usr/lib64/pkgconfig/SPIRV-Tools-shared.pc
rm -f %{buildroot}*/usr/lib64/pkgconfig/SPIRV-Tools.pc
rm -f %{buildroot}*/usr/include/spirv-tools/instrument.hpp
rm -f %{buildroot}*/usr/include/spirv-tools/libspirv.h
rm -f %{buildroot}*/usr/include/spirv-tools/libspirv.hpp
rm -f %{buildroot}*/usr/include/spirv-tools/linker.hpp
rm -f %{buildroot}*/usr/include/spirv-tools/optimizer.hpp

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glslc

%files dev
%defattr(-,root,root,-)
/usr/include/shaderc/env.h
/usr/include/shaderc/shaderc.h
/usr/include/shaderc/shaderc.hpp
/usr/include/shaderc/status.h
/usr/include/shaderc/visibility.h
/usr/lib64/libshaderc_shared.so
/usr/lib64/pkgconfig/shaderc.pc
/usr/lib64/pkgconfig/shaderc_combined.pc
/usr/lib64/pkgconfig/shaderc_static.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libshaderc_shared.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/shaderc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/shaderc/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/shaderc/9a84200f47e09abfbde1a6b25028460451b23d03
/usr/share/package-licenses/shaderc/cdea109780799ce618a98a53a52efbae6afb8247
/usr/share/package-licenses/shaderc/f67a567c3c0f82d745f3f273bf1cadd6b1edcad4
/usr/share/package-licenses/shaderc/f77668fa8c7bb3dc2788af730150c401bd723fed
