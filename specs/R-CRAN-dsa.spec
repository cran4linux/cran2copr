%global __brp_check_rpaths %{nil}
%global packname  dsa
%global packver   1.0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.12
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonal Adjustment of Daily Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-seastests 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-R2HTML 
Requires:         R-grid 
Requires:         R-tools 
Requires:         R-CRAN-tsoutliers 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-seastests 

%description
Seasonal- and calendar adjustment of time series with daily frequency
using the DSA approach developed by Ollech, Daniel (2018): Seasonal
adjustment of daily time series. Bundesbank Discussion Paper 41/2018.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
