%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FastJM
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Semi-Parametric Joint Modeling of Longitudinal and Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Hmisc 

%description
Maximum likelihood estimation for the semi-parametric joint modeling of
competing risks and longitudinal data applying customized linear scan
algorithms, proposed by Li and colleagues (2022)
<doi:10.1155/2022/1362913>. The time-to-event data is modelled using a
(cause-specific) Cox proportional hazards regression model with time-fixed
covariates. The longitudinal outcome is modelled using a linear mixed
effects model. The association is captured by shared random effects. The
model is estimated using an Expectation Maximization algorithm.

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
