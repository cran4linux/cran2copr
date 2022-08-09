%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geex
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          An API for M-Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-methods >= 3.3
BuildRequires:    R-CRAN-numDeriv >= 2014.2.1
BuildRequires:    R-CRAN-rootSolve >= 1.6.6
BuildRequires:    R-CRAN-Matrix >= 1.2.6
BuildRequires:    R-CRAN-lme4 >= 1.1.12
Requires:         R-methods >= 3.3
Requires:         R-CRAN-numDeriv >= 2014.2.1
Requires:         R-CRAN-rootSolve >= 1.6.6
Requires:         R-CRAN-Matrix >= 1.2.6
Requires:         R-CRAN-lme4 >= 1.1.12

%description
Provides a general, flexible framework for estimating parameters and
empirical sandwich variance estimator from a set of unbiased estimating
equations (i.e., M-estimation in the vein of Stefanski & Boos (2002)
<doi:10.1198/000313002753631330>). All examples from Stefanski & Boos
(2002) are published in the corresponding Journal of Statistical Software
paper "The Calculus of M-Estimation in R with geex" by Saul & Hudgens
(2020) <doi:10.18637/jss.v092.i02>. Also provides an API to compute
finite-sample variance corrections.

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
