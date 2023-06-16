%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JMH
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Model of Heterogeneous Repeated Measures and Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nlme 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-caret 

%description
Maximum likelihood estimation for the semi-parametric joint modeling of
competing risks and longitudinal data in the presence of heterogeneous
within-subject variability, proposed by Li and colleagues (2023)
<arXiv:2301.06584>. The proposed method models the within-subject
variability of the biomarker and associates it with the risk of the
competing risks event. The time-to-event data is modeled using a
(cause-specific) Cox proportional hazards regression model with time-fixed
covariates. The longitudinal outcome is modeled using a mixed-effects
location and scale model. The association is captured by shared random
effects. The model is estimated using an Expectation Maximization
algorithm.

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
