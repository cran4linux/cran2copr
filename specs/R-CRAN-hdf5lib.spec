%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdf5lib
%global packver   2.1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Headers and Static Libraries for 'HDF5'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0

%description
Provides a self-contained, static build of the 'HDF5' (Hierarchical Data
Format 5) 'C' library (release 2.1.1) for R package developers. Designed
for use in the 'LinkingTo' field, it enables zero-dependency integration
by building the library entirely from source during installation.
Additionally, it compiles and internally links a comprehensive suite of
advanced compression filters and their 'HDF5' plugins (Zstd, LZ4,
Blosc/Blosc2, Snappy, ZFP, Bzip2, LZF, Bitshuffle, szip, and gzip). These
plugins are integrated out-of-the-box, allowing downstream packages to
utilize high-performance compression directly through the standard 'HDF5'
API while keeping the underlying third-party headers fully encapsulated.
'HDF5' is developed by The HDF Group <https://www.hdfgroup.org/>.

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
