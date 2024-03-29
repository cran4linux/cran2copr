%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  twdtw
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Weighted Dynamic Time Warping

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-proxy 

%description
Implements Time-Weighted Dynamic Time Warping (TWDTW), a measure for
quantifying time series similarity. The TWDTW algorithm, described in Maus
et al. (2016) <doi:10.1109/JSTARS.2016.2517118> and Maus et al. (2019)
<doi:10.18637/jss.v088.i05>, is applicable to multi-dimensional time
series of various resolutions. It is particularly suitable for comparing
time series with seasonality for environmental and ecological data
analysis, covering domains such as remote sensing imagery, climate data,
hydrology, and animal movement. The 'twdtw' package offers a user-friendly
'R' interface, efficient 'Fortran' routines for TWDTW calculations,
flexible time weighting definitions, as well as utilities for time series
preprocessing and visualization.

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
