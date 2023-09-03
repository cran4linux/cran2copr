%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDJM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Penalized High-Dimensional Joint Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-survival >= 3.2
BuildRequires:    R-CRAN-statmod >= 1.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEnsmallen 
Requires:         R-CRAN-survival >= 3.2
Requires:         R-CRAN-statmod >= 1.4
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
Joint models have been widely used to study the associations between
longitudinal biomarkers and a survival outcome. However, existing joint
models only consider one or a few longitudinal biomarkers and cannot deal
with high-dimensional longitudinal biomarkers. This package can be used to
fit our recently developed penalized joint model that can handle
high-dimensional longitudinal biomarkers. Specifically, an adaptive lasso
penalty is imposed on the parameters for the effects of the longitudinal
biomarkers on the survival outcome, which allows for variable selection.
Also, our algorithm is computationally efficient, which is based on the
Gaussian variational approximation method.

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
