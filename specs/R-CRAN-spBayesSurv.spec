%global __brp_check_rpaths %{nil}
%global packname  spBayesSurv
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Modeling and Analysis of Spatially Correlated Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.4.300.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-splines 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-survival 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fields 
Requires:         R-splines 

%description
Provides several Bayesian survival models for spatial/non-spatial survival
data: proportional hazards (PH), accelerated failure time (AFT),
proportional odds (PO), and accelerated hazards (AH), a super model that
includes PH, AFT, PO and AH as special cases, Bayesian nonparametric
nonproportional hazards (LDDPM), generalized accelerated failure time
(GAFT), and spatially smoothed Polya tree density estimation. The spatial
dependence is modeled via frailties under PH, AFT, PO, AH and GAFT, and
via copulas under LDDPM and PH. Model choice is carried out via the
logarithm of the pseudo marginal likelihood (LPML), the deviance
information criterion (DIC), and the Watanabe-Akaike information criterion
(WAIC). See Zhou, Hanson and Zhang (2020) <doi:10.18637/jss.v092.i09>.

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
