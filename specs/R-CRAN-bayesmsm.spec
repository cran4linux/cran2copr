%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesmsm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting Bayesian Marginal Structural Models for Longitudinal Observational Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda >= 0.19.4
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda >= 0.19.4
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MCMCpack 
Requires:         R-parallel 
Requires:         R-CRAN-R2jags 
Requires:         R-stats 

%description
Implements Bayesian marginal structural models for causal effect
estimation with time-varying treatment and confounding. It includes an
extension to handle informative right censoring. The Bayesian importance
sampling weights are estimated using JAGS. See Saarela (2015)
<doi:10.1111/biom.12269> for methodological details.

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
