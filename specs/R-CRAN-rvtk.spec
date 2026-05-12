%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rvtk
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bindings for the Visualization Toolkit ('VTK')

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides pre-compiled static 'VTK' libraries and headers so that
downstream R packages can link against the Visualization Toolkit without
requiring users to install 'VTK' manually. On all platforms the package
first honours a user-supplied 'VTK_DIR' environment variable. On macOS it
then tries 'Homebrew', followed by 'pkg-config'. On Linux it tries
'pkg-config' and well-known system prefixes ('/usr', '/usr/local'). If no
suitable system installation is found on macOS or Linux, pre-built static
libraries are downloaded automatically from the package's GitHub releases.
On Windows the package tries 'VTK_DIR', then 'Rtools45' 'pacman', then
common 'MSYS2' prefixes, accepting both static ('.a') and shared ('.dll.a'
import libs + DLLs) installations. When shared libraries are used, the VTK
DLLs are staged in 'inst/vtk-dlls/' and an '.onLoad' hook prepends that
directory to PATH via 'Sys.setenv()' when the package is loaded, and
restored in '.onUnload()'. The pre-built fallback downloads static
libraries by default; set 'VTK_LINK_TYPE=shared' before installation to
download the DLL build instead. Note that on Windows the modules
'VTK_IONetCDF', 'VTK_IOHDF', 'VTK_GeovisCore', and 'VTK_RenderingCore' are
disabled because 'netcdf' and 'libproj' are not available in the
'Rtools45' 'static.posix' sysroot. Downstream packages can declare
'Imports: rvtk' and obtain the correct compiler and linker flags at
install time via rvtk::CppFlags() and rvtk::LdFlagsFile().

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
