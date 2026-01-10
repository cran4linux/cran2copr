%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  resourcecode
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'RESOURCECODE' Hindcast Database

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-resourcecodedata 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridtext 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-resourcecodedata 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Utility functions to download data from the 'RESOURCECODE' hindcast
database of sea-states, time series of sea-state parameters and time
series of 1D and 2D wave spectra.  See <https://resourcecode.ifremer.fr>
for more details about the available data.  Also provides facilities to
plot and analyse downloaded data, such as computing the sea-state
parameters from both the 1D and 2D surface elevation variance spectral
density.

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
