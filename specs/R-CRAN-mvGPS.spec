%global __brp_check_rpaths %{nil}
%global packname  mvGPS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference using Multivariate Generalized Propensity Score

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-CRAN-cobalt 
BuildRequires:    R-CRAN-matrixNormal 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-CBPS 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-WeightIt 
Requires:         R-CRAN-cobalt 
Requires:         R-CRAN-matrixNormal 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-CBPS 

%description
Methods for estimating and utilizing the multivariate generalized
propensity score (mvGPS) for multiple continuous exposures described in
Williams, J.R, and Crespi, C.M. (2020) <arxiv:2008.13767>. The methods
allow estimation of a dose-response surface relating the joint
distribution of multiple continuous exposure variables to an outcome.
Weights are constructed assuming a multivariate normal density for the
marginal and conditional distribution of exposures given a set of
confounders. Confounders can be different for different exposure
variables. The weights are designed to achieve balance across all exposure
dimensions and can be used to estimate dose-response surfaces.

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
