%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skewlmm
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Scale Mixture of Skew-Normal Linear Mixed Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-optimParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MomTrunc 
BuildRequires:    R-CRAN-TruncatedNormal 
Requires:         R-CRAN-optimParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MomTrunc 
Requires:         R-CRAN-TruncatedNormal 

%description
It fits scale mixture of skew-normal linear mixed models using either an
expectation–maximization (EM) type algorithm or its accelerated version
(Damped Anderson Acceleration with Epsilon Monotonicity, DAAREM),
including some possibilities for modeling the within-subject dependence
<doi:10.18637/jss.v115.i07>.

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
