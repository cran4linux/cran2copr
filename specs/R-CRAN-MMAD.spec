%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MMAD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          MM Algorithm Based on the Assembly-Decomposition Technology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-survival 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-survival 

%description
The Minorize-Maximization(MM) algorithm based on
Assembly-Decomposition(AD) technology can be used for model estimation of
parametric models, semi-parametric models and non-parametric models. We
selected parametric models including left truncated normal distribution,
type I multivariate zero-inflated generalized poisson distribution and
multivariate compound zero-inflated generalized poisson distribution;
semiparametric models include Cox model and gamma frailty model;
nonparametric model is estimated for type II interval-censored data. These
general methods are proposed based on the following papers, Tian, Huang
and Xu (2019) <doi:10.5705/SS.202016.0488>, Huang, Xu and Tian (2019)
<doi:10.5705/ss.202016.0516>, Zhang and Huang (2022)
<doi:10.1117/12.2642737>.

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
