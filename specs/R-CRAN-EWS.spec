%global __brp_check_rpaths %{nil}
%global packname  EWS
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Early Warning System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-numDeriv 

%description
The purpose of Early Warning Systems (EWS) is to detect accurately the
occurrence of a crisis, which is represented by a binary variable which
takes the value of one when the event occurs, and the value of zero
otherwise. EWS are a toolbox for policymakers to prevent or attenuate the
impact of economic downturns. Modern EWS are based on the econometric
framework of Kauppi and Saikkonen (2008) <doi:10.1162/rest.90.4.777>.
Specifically, this framework includes four dichotomous models, relying on
a logit approach to model the relationship between yield spreads and
future recessions, controlling for recession risk factors. These models
can be estimated in a univariate or a balanced panel framework as in
Candelon, Dumitrescu and Hurlin (2014)
<doi:10.1016/j.ijforecast.2014.03.015>. This package provides both methods
for estimating these models and a dataset covering 13 OECD countries over
a period of 45 years. In addition, this package also provides methods for
the analysis of the propagation mechanisms of an exogenous shock, as well
as robust confidence intervals for these response functions using a
block-bootstrap method as in Lajaunie (2021). This package constitutes a
useful toolbox (data and functions) for scholars as well as policymakers.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
