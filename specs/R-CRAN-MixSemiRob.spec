%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixSemiRob
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixture Models: Parametric, Semiparametric, and Robust

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-GoFKernel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rlab 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
Requires:         R-CRAN-GoFKernel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rlab 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 

%description
Various functions are provided to estimate parametric mixture models (with
Gaussian, t, Laplace, log-concave distributions, etc.) and non-parametric
mixture models. The package performs hypothesis tests and addresses label
switching issues in mixture models. The package also allows for parameter
estimation in mixture of regressions, proportion-varying mixture of
regressions, and robust mixture of regressions.

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
