%global __brp_check_rpaths %{nil}
%global packname  ssdtools
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          1%{?dist}%{?buildtag}
Summary:          Species Sensitivity Distributions

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-Rcpp 

%description
Species sensitivity distributions are cumulative probability distributions
which are fitted to toxicity concentrations for different species as
described by Posthuma et al.(2001) <isbn:9781566705783>. The ssdtools
package uses Maximum Likelihood to fit distributions such as the
log-normal, gamma, log-logistic, log-Gumbel, Gompertz and Weibull. The
user can provide custom distributions. Multiple distributions can be
averaged using Information Criteria. Confidence intervals on hazard
concentrations and proportions are produced by parametric bootstrapping.

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
