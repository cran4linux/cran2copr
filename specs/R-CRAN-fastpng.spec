%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastpng
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Write PNG Files with Configurable Decoder/Encoder Options

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-colorfast >= 1.0.1
Requires:         R-CRAN-colorfast >= 1.0.1

%description
Read and write PNG images with arrays, rasters, native rasters, numeric
arrays, integer arrays, raw vectors and indexed values.  This PNG encoder
exposes configurable internal options enabling the user to select a
speed-size tradeoff.  For example, disabling compression can speed up
writing PNG by a factor of 50. Multiple image formats are supported
including raster, native rasters, and integer and numeric arrays at color
depths of 1, 2, 3 or 4. 16-bit images are also supported. This
implementation uses the 'libspng' 'C' library which is available from
<https://github.com/randy408/libspng/>.

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
