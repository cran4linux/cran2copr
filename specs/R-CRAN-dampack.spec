%global packname  dampack
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Decision-Analytic Modeling Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-ggrepel 

%description
A suite of functions for analyzing and visualizing the health economic
outputs of mathematical models. This package was developed with funding
from the National Institutes of Allergy and Infectious Diseases of the
National Institutes of Health under award no. R01AI138783. The content of
this package is solely the responsibility of the authors and does not
necessarily represent the official views of the National Institutes of
Health. The theoretical underpinnings of 'dampack''s functionality are
detailed in Hunink et al. (2014) <doi:10.1017/CBO9781139506779>.

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
