%global __brp_check_rpaths %{nil}
%global cname TileDB
%global major 2
%global minor 11
%global patch 1

Name:           tiledb
Version:        %{major}.%{minor}.%{patch}
Release:        1%{?dist}%{?buildtag}
Summary:        The Universal Storage Engine

License:        MIT
URL:            https://github.com/%{cname}-Inc/%{cname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/TileDB-Inc/TileDB/bc235a65a25757f93fc4da7fd0d82c70e47bff70/cmake/Modules/FindMagic_EP.cmake

BuildRequires:  gcc-g++, cmake
BuildRequires:  clang-tools-extra
BuildRequires:  doxygen
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(catch2)
#BuildRequires:  pkgconfig(libcurl)
#BuildRequires:  pkgconfig(capnp)

%global _description %{expand:
TileDB is a powerful engine for storing and accessing dense and sparse
multi-dimensional arrays, which can help you model any complex data
efficiently. It is an embeddable C++ library that works on Linux, macOS,
and Windows. It is open-sourced under the permissive MIT License,
developed and maintained by TileDB, Inc. To distinguish this project
from other TileDB offerings, we often refer to it as TileDB Embedded.
}

%description %_description

%package devel
Summary:        Development headers and libraries for %{cname}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_description
This package contains the development headers and libraries.

%prep
%autosetup -p1 -n %{cname}-%{version}
mv %{SOURCE1} cmake/Modules/

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DTILEDB_TOOLS=0 \
    -DTILEDB_SERIALIZATION=0 \
    -DTILEDB_TESTS=0 \
    -DTILEDB_WERROR=0
%cmake_build

%install
%make_install -C "%{_vpath_builddir}/%{name}"

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{major}.%{minor}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/cmake/%{cname}/%{cname}Config.cmake
%{_libdir}/cmake/%{cname}/%{cname}ConfigVersion.cmake
%{_libdir}/cmake/%{cname}/%{cname}Targets.cmake
%{_libdir}/cmake/%{cname}/%{cname}Targets-release.cmake
%{_libdir}/pkgconfig/%{name}.pc

%changelog
