%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastfocal
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Multiscale Raster Extraction and Moving Window Analysis with FFT

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-terra 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Provides fast moving-window ("focal") and buffer-based extraction for
raster data using the 'terra' package. Automatically selects between a
'C++' backend (via 'terra') and a Fast Fourier Transform (FFT) backend
depending on problem size. The FFT backend supports sum and mean, while
other statistics (e.g., median, min, max, standard deviation) are handled
by the 'terra' backend. Supports multiple kernel types (e.g., circle,
rectangle, gaussian), with NA handling consistent with 'terra' via 'na.rm'
and 'na.policy'. Operates on 'SpatRaster' objects and returns results with
the same geometry.

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
