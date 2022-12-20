%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PLreg
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Logit Regression for Modeling Bounded Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-zipfR 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-GeneralizedHyperbolic 
Requires:         R-methods 
Requires:         R-CRAN-nleqslv 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-zipfR 

%description
Power logit regression models for bounded continuous data, in which the
density generator may be normal, Student-t, power exponential, slash,
hyperbolic, sinh-normal, or type II logistic. Diagnostic tools associated
with the fitted model, such as the residuals, local influence measures,
leverage measures, and goodness-of-fit statistics, are implemented. The
estimation process follows the maximum likelihood approach and, currently,
the package supports two types of estimators: the usual maximum likelihood
estimator and the penalized maximum likelihood estimator. More details
about power logit regression models are described in Queiroz and Ferrari
(2022) <arXiv:2202.01697>.

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
