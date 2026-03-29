%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastJM
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
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
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pec 
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
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 

%description
Implements scalable joint models for large-scale competing risks
time-to-event data with one or multiple longitudinal biomarkers using the
efficient algorithms developed by Li et al. (2022)
<doi:10.1155/2022/1362913> and <doi:10.48550/arXiv.2506.12741>. The
time-to-event process is modeled using a cause-specific Cox proportional
hazards model with time-fixed covariates, while longitudinal biomarkers
are modeled using linear mixed-effects models. The association between the
longitudinal and survival processes is captured through shared random
effects. The package enables analysis of large-scale biomedical data to
model biomarker trajectories, estimate their effects on event risks, and
perform dynamic prediction of future events based on patients'
longitudinal histories. Functions for simulating survival and longitudinal
data for multiple biomarkers are included, along with built-in example
datasets. The package also supports modeling a single biomarker with
heterogeneous within-subject variability via functionality adapted from
the 'JMH' package.

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
