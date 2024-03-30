%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SemiPar.depCens
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Based Cox Proportional Hazards Models for Dependent Censoring

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pbivnorm 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-copula 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pbivnorm 

%description
Copula based Cox proportional hazards models for survival data subject to
dependent censoring. This approach does not assume that the parameter
defining the copula is known. The dependency parameter is estimated with
other finite model parameters by maximizing a Pseudo likelihood function.
The cumulative hazard function is estimated via estimating equations
derived based on martingale ideas. Available copula functions include
Frank, Gumbel and Normal copulas. Only Weibull and lognormal models are
allowed for the censoring model, even though any parametric model that
satisfies certain identifiability conditions could be used. Implemented
methods are described in the article "Copula based Cox proportional
hazards models for dependent censoring" by Deresa and Van Keilegom (2023)
<doi:10.1080/01621459.2022.2161387>.

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
