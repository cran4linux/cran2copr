%global __brp_check_rpaths %{nil}
%global packname  survivalREC
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation of the Distribution of Gap Times for Recurrent Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-KernSmooth 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides estimates for the bivariate and trivariate distribution functions
and bivariate and trivariate survival functions for censored gap times.
Two approaches, using existing methodologies, are considered: (i) the
Lin's estimator, which is based on the extension the Kaplan-Meier
estimator of the distribution function for the first event time and the
Inverse Probability of Censoring Weights for the second time (Lin DY, Sun
W, Ying Z (1999) <doi:10.1093/biomet/86.1.59> and (ii) another estimator
based on Kaplan-Meier weights (Una-Alvarez J, Meira-Machado L (2008)
<https://w3.math.uminho.pt/~lmachado/Biometria_conference.pdf>). The
proposed methods are the landmark estimators based on subsampling
approach, and the estimator based on weighted cumulative hazard estimator.
The package also provides nonparametric estimator conditional to a given
continuous covariate. All these methods have been submitted to be
published.

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
