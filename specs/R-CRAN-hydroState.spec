%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hydroState
%global packver   0.2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Modelling of Hydrological State Change

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-padr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-methods 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-padr 
Requires:         R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-CRAN-checkmate 

%description
Identifies regime changes in streamflow runoff not explained by variations
in precipitation. The package builds a flexible set of Hidden Markov
Models of annual, seasonal or monthly streamflow runoff with precipitation
as a predictor. Suites of models can be built for a single site, ranging
from one to three states and each with differing combinations of error
models and auto-correlation terms. The most parsimonious model is easily
identified by AIC, and useful for understanding catchment drought
non-recovery: Peterson TJ, Saft M, Peel MC & John A (2021)
<doi:10.1126/science.abd5085>.

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
