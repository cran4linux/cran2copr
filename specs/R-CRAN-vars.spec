%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vars
%global packver   1.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          VAR Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich >= 2.2.4
BuildRequires:    R-CRAN-urca >= 1.1.6
BuildRequires:    R-CRAN-lmtest >= 0.9.26
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-methods 
Requires:         R-CRAN-sandwich >= 2.2.4
Requires:         R-CRAN-urca >= 1.1.6
Requires:         R-CRAN-lmtest >= 0.9.26
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-strucchange 
Requires:         R-methods 

%description
Estimation, lag selection, diagnostic testing, forecasting, causality
analysis, forecast error variance decomposition and impulse response
functions of VAR models and estimation of SVAR and SVEC models.

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
