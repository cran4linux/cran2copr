%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  VAJointSurv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Approximation for Joint Survival and Marker Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-psqn >= 0.3.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-splines 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SimSurvNMarker 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-splines 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-SimSurvNMarker 
Requires:         R-CRAN-psqn >= 0.3.0
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-lme4 

%description
Estimates joint marker (longitudinal) and and survival (time-to-event)
outcomes using variational approximations. The package supports
multivariate markers allowing for correlated error terms and multiple
types of survival outcomes which may be left-truncated, right-censored,
and recurrent. Time-varying fixed and random covariate effects are
supported along with non-proportional hazards.

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
