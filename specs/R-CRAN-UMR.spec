%global __brp_check_rpaths %{nil}
%global packname  UMR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unmatched Monotone Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-decon 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-distr 
Requires:         R-CRAN-decon 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-distr 

%description
Unmatched regression refers to the regression setting where covariates and
predictors are collected separately/independently and so are not paired
together, as in the usual regression setting.  Balabdaoui, Doss, and Durot
(2021) <arXiv:2007.00830> study the unmatched regression setting where the
univariate regression function is known to be monotone.  This package
implements methods for computing the estimator developed in Balabdaoui,
Doss, and Durot (2021).  The main method is an
active-set-trust-region-based method.

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
