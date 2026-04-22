%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustDIF
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Differential Item Functioning Using Robust Scaling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-lavaan 

%description
Provides tools for testing differential item functioning (DIF) and
differential test functioning (DTF) in two-group item response theory
models. The package estimates robust scaling parameters via iteratively
reweighted least squares with Tukey's bisquare loss, and supports
Wald-type tests of item-level and test-level differences from robust
scaling parameters. Inputs can be supplied directly from model
parameter/covariance objects or extracted from fitted 'mirt' and 'lavaan'
models. Methods are described in Halpin (2022)
<doi:10.48550/arXiv.2207.04598>.

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
