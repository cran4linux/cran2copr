%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fect
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fixed Effects Counterfactuals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-GGally >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-fixest 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-panelView 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-GGally >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-fixest 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-future 
Requires:         R-CRAN-panelView 
Requires:         R-CRAN-mvtnorm 

%description
Estimates causal effects with panel data using the counterfactual methods.
It is suitable for panel or time-series cross-sectional analysis with
binary treatments under (hypothetically) baseline randomization.It allows
a treatment to switch on and off and limited carryover effects. It
supports linear factor models, a generalization of gsynth and the matrix
completion method. Implementation details can be found in Liu, Wang and Xu
(2022) <arXiv:2107.00856>.

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
