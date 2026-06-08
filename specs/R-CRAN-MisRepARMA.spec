%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MisRepARMA
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Misreported Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-R2jags 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-R2jags 

%description
Provides a simple and trustworthy methodology for the analysis of
misreported continuous time series using either a frequentist
(bootstrap-based EM algorithm) or a Bayesian (MCMC via JAGS) approach. The
frequentist method is described in Morina et al. (2021)
<doi:10.1038/s41598-021-02620-5>. The Bayesian extension fits the same
ARMA model with misreporting structure using a full posterior
distribution, providing credible intervals and DIC for model comparison,
as described in Morina et al. (2024) <doi:10.1101/2024.02.26.24303373>.

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
