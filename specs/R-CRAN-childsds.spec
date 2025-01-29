%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  childsds
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Data and Methods Around Reference Values in Pediatrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-purrrlyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-lubridate 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-class 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-purrrlyr 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-lubridate 

%description
Calculation of standard deviation scores and percentiles adduced from
different standards (WHO, UK, Germany, Italy, China, etc). Also,
references for laboratory values in children and adults are available,
e.g., serum lipids, iron-related blood parameters, IGF, liver enzymes. See
package documentation for full list.

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
