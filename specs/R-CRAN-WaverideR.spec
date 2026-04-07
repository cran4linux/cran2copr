%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WaverideR
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extracting Signals from Wavelet Spectra

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-colorednoise 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-astrochron 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-trapezoid 
BuildRequires:    R-CRAN-fANCOVA 
BuildRequires:    R-CRAN-DecomposeR 
BuildRequires:    R-CRAN-scico 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-colorednoise 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-truncnorm 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-astrochron 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-trapezoid 
Requires:         R-CRAN-fANCOVA 
Requires:         R-CRAN-DecomposeR 
Requires:         R-CRAN-scico 

%description
Tools for extracting and analyzing cyclic signals from time series.

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
