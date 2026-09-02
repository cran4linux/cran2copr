%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastgbm
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Histogram Gradient Boosting for Regression, Classification, and Survival Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 

%description
A fast gradient boosting machine covering four task types with one
interface: regression (squared error), binary and multiclass
classification (logistic and one-vs-rest), and right-censored survival
analysis via Cox (Breslow ties), accelerated failure time (normal
location-scale), or piecewise-exponential objectives. Provides native
missing-value routing, baseline-hazard estimation and survival-probability
prediction for the survival objectives, and deterministic multi-threaded
training via 'RcppParallel'. Methods are described in Friedman (2001)
<doi:10.1214/aos/1013203451>.

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
