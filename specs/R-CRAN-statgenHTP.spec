%global packname  statgenHTP
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Throughput Phenotyping (HTP) Data Analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-SpATS >= 1.0.11
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-splines 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-SpATS >= 1.0.11
Requires:         R-CRAN-animation 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggforce 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-splines 

%description
Phenotypic analysis of data coming from high throughput phenotyping (HTP)
platforms, including different types of outlier detection, spatial
analysis, and parameter estimation. The package is being developed within
the EPPN2020 project (<https://eppn2020.plant-phenotyping.eu/>). Some
functions have been created to be used in conjunction with the R package
'asreml' for the 'ASReml' software, which can be obtained upon purchase
from 'VSN' international (<https://www.vsni.co.uk/software/asreml>).

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
