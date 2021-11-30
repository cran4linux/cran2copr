%global __brp_check_rpaths %{nil}
%global packname  weightedGCM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Generalised Covariance Measure Conditional Independence Test

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-GeneralisedCovarianceMeasure 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-GeneralisedCovarianceMeasure 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-CRAN-xgboost 

%description
A conditional independence test that can be applied both to univariate and
multivariate random variables. The test is based on a weighted form of the
sample covariance of the residuals after a nonlinear regression on the
conditioning variables. Details are described in Scheidegger, Hoerrmann
and Buehlmann (2021) "The Weighted Generalised Covariance Measure"
<arXiv:2111.04361>. The test is a generalisation of the Generalised
Covariance Measure (GCM) implemented in the R package
'GeneralisedCovarianceMeasure' by Jonas Peters and Rajen D. Shah based on
Shah and Peters (2020) "The Hardness of Conditional Independence Testing
and the Generalised Covariance Measure" <arXiv:1804.07203>.

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
