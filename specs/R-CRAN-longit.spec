%global __brp_check_rpaths %{nil}
%global packname  longit
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Longitudinal Data Analysis Using MCMC

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-AICcmodavg 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-utils 
Requires:         R-CRAN-AICcmodavg 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-rjags 
Requires:         R-utils 

%description
High dimensional longitudinal data analysis with Markov Chain Monte
Carlo(MCMC). Currently support mixed effect regression with or without
missing observations by considering covariance structures. It provides
estimates by missing at random and missing not at random assumptions. In
this R package, we present Bayesian approaches that statisticians and
clinical researchers can easily use. The functions' methodology is based
on the book "Bayesian Approaches in Oncology Using R and OpenBUGS" by
Bhattacharjee A (2020) <doi:10.1201/9780429329449-14>.

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
