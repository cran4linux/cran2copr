%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  psvr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Percentage-Error Support Vector Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tune 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-workflowsets 
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-dials 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-tune 
Requires:         R-utils 
Requires:         R-CRAN-workflowsets 

%description
Implements four support vector regression (SVR) models derived from a
unified mathematical framework for percentage-error loss functions:
epsilon-SVR minimizing the mean absolute percentage error (MAPE), its
symmetric kernel extension, least-squares SVR (LS-SVR) minimizing the root
mean square percentage error (RMSPE), and its symmetric counterpart. All
models require strictly positive targets. The epsilon-SVR models are
solved via a built-in sequential minimal optimization (SMO) algorithm
(with 'osqp' available as an optional alternative backend) and the LS-SVR
models via a linear system (base R). See Benavides-Herrera et al. (2026)
<doi:10.3390/math14101679> for the mathematical derivations.

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
