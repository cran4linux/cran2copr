%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misskappa
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Agreement Coefficients with Missing Ratings

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Estimates chance-corrected agreement coefficients (Cohen's, Conger's, and
Fleiss' kappa and the Brennan-Prediger coefficient; Conger (1980)
<doi:10.1037/0033-2909.88.2.322>) for any number of raters, with nominal,
linear, or quadratic weights, when some ratings are missing. Missing
ratings are handled by inverse-probability weighting (Horvitz and Thompson
(1952) <doi:10.1080/01621459.1952.10483446>) when they are missing
completely at random, and by categorical or robust normal-theory
full-information maximum likelihood when they are missing at random
(Little and Rubin (2019) <doi:10.1002/9781119482260>). Every estimate
comes with an influence-function standard error, giving confidence
intervals and Wald tests that compare coefficients across groups, raters,
or estimators. Also handles counts-format data, multirater g-wise
agreement (Moss (2024) <doi:10.1007/s11336-023-09945-2>), and
vector-valued ratings.

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
