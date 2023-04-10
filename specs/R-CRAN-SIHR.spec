%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SIHR
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Inference in High Dimensional Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 

%description
The goal of SIHR is to provide inference procedures in the
high-dimensional setting for (1) linear functionals in generalized linear
regression ('Cai et al.' (2019) <arXiv:1904.12891>, 'Guo et al.' (2020)
<arXiv:2012.07133>, 'Cai et al.' (2021)), (2) conditional average
treatment effects in generalized linear regression, (3) quadratic
functionals in generalized linear regression ('Guo et al.' (2019)
<arXiv:1909.01503>). (4) inner product in generalized linear regression
(5) distance in generalized linear regression.

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
