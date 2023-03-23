%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcen
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Cluster Elastic Net

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-faraway 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-Matrix 
Requires:         R-parallel 
Requires:         R-CRAN-faraway 
Requires:         R-methods 
Requires:         R-stats 

%description
Fits the Multivariate Cluster Elastic Net (MCEN) presented in Price &
Sherwood (2018) <arXiv:1707.03530>. The MCEN model simultaneously
estimates regression coefficients and a clustering of the responses for a
multivariate response model. Currently accommodates the Gaussian and
binomial likelihood.

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
