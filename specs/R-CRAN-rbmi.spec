%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbmi
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Based Multiple Imputation

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mmrm 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-assertthat 
Requires:         R-CRAN-mmrm 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-Matrix 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-assertthat 

%description
Implements standard and reference based multiple imputation methods for
continuous longitudinal endpoints (Gower-Page et al. (2022)
<doi:10.21105/joss.04251>). In particular, this package supports
deterministic conditional mean imputation and jackknifing as described in
Wolbers et al.  (2022) <doi:10.1002/pst.2234>, Bayesian multiple
imputation as described in Carpenter et al. (2013)
<doi:10.1080/10543406.2013.834911>, and bootstrapped maximum likelihood
imputation as described in von Hippel and Bartlett (2021) <doi:
10.1214/20-STS793>.

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
