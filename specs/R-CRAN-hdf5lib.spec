%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdf5lib
%global packver   2.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Headers and Static Libraries for 'HDF5'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0

%description
'HDF5' (Hierarchical Data Format 5) is a high-performance library and file
format for storing and managing large, complex data. This package provides
the static libraries and headers for the 'HDF5' 'C' library (release
2.0.0). It is intended for R package developers to use in the 'LinkingTo'
field, which eliminates the need for users to install system-level 'HDF5'
dependencies. This build is compiled with thread-safety enabled and
supports dynamic loading of external compression filters. 'HDF5' is
developed by 'The HDF Group' <https://www.hdfgroup.org/>.

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
