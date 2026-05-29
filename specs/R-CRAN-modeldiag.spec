%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modeldiag
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Diagnostics for Statistical Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-ResourceSelection 
BuildRequires:    R-CRAN-survival 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-ResourceSelection 
Requires:         R-CRAN-survival 

%description
Provides a unified framework for diagnosing common issues in statistical
models including linear models, generalized linear models (logistic and
Poisson regression), and survival models. Implements tests for
multicollinearity, heteroscedasticity, autocorrelation, normality,
influential observations, overdispersion, zero-inflation, and proportional
hazards assumptions. Includes visualization methods for graphical
diagnostics. Methods are based on established approaches including Fox and
Monette (1992) <doi:10.1080/01621459.1992.10475190>, Breusch and Pagan
(1979) <doi:10.2307/1911963>, and Dean and Lawless (1989)
<doi:10.1080/01621459.1989.10478792>.

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
