%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastJM
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Joint Modeling of Longitudinal and Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-survival 
Requires:         R-utils 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-timeROC 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
A joint model for large-scale, competing risks time-to-event data with
singular or multiple longitudinal biomarkers, implemented with the
efficient algorithms developed by Li and colleagues (2022)
<doi:10.1155/2022/1362913> and <doi:10.48550/arXiv.2506.12741>. The
time-to-event data is modelled using a (cause-specific) Cox proportional
hazards regression model with time-fixed covariates. The longitudinal
biomarkers are modelled using a linear mixed effects model. The
association between the longitudinal submodel and the survival submodel is
captured through shared random effects. It allows researchers to analyze
large-scale data to model biomarker trajectories, estimate their effects
on event outcomes, and dynamically predict future events from patients’
past histories. A function for simulating survival and longitudinal data
for multiple biomarkers is also included alongside built-in datasets.

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
