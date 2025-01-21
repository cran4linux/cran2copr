%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AMISforInfectiousDiseases
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Implement the AMIS Algorithm for Infectious Disease Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-weights 

%description
Implements the Adaptive Multiple Importance Sampling (AMIS) algorithm, as
described by Retkute et al. (2021, <doi:10.1214/21-AOAS1486>), to estimate
key epidemiological parameters by combining outputs from a geostatistical
model of infectious diseases (such as prevalence, incidence, or relative
risk) with a disease transmission model. Utilising the resulting posterior
distributions, the package enables forward projections at the local level.

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
