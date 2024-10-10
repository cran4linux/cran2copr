%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  insurancerating
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analytic Insurance Rating Techniques

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ciTools 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-evtree 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ciTools 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-evtree 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-scam 
Requires:         R-CRAN-stringr 

%description
Functions to build, evaluate, and visualize insurance rating models. It
simplifies the process of modeling premiums, and allows to analyze
insurance risk factors effectively. The package employs a data-driven
strategy for constructing insurance tariff classes, drawing on the work of
Antonio and Valdez (2012) <doi:10.1007/s10182-011-0152-7>.

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
