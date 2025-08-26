%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  climwin
%global packver   1.2.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.32
Release:          1%{?dist}%{?buildtag}
Summary:          Climate Window Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppRoll 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-RcppRoll 
Requires:         R-CRAN-nlme 

%description
Contains functions to detect and visualise periods of climate sensitivity
(climate windows) for a given biological response. Please see van de Pol
et al. (2016) <doi:10.1111/2041-210X.12590> and Bailey and van de Pol
(2016) <doi:10.1371/journal.pone.0167980> for details.

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
