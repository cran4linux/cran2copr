%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fracreg
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fractional Response Regressions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-MASS 

%description
Provides routines for the estimation and specification analysis of
fractional response models. Includes univariate one-part, two-part, and
double-inflated three-part fractional models. Further incorporates
estimators for panel data settings and addresses unobserved heterogeneity
and endogeneity via correlated random effects and control function
approaches. Extends fractional methodology to multivariate data via
fractional multinomial logit models and handles high-dimensional
multicollinear data via fractional ridge regression. Calculates analytical
partial effects across all model types and includes generalised
goodness-of-functional-form (GGOFF) and Regression Equation Specification
Error Test (RESET) hypothesis tests. Methods are described in Papke and
Wooldridge (1996)
<doi:10.1002/(SICI)1099-1255(199611)11:6%%3C619::AID-JAE418%%3E3.0.CO;2-1>,
Papke and Wooldridge (2008) <doi:10.1016/j.jeconom.2008.05.009>, Buis
(2008) <http://maartenbuis.nl/software/likelihoodFmlogit.pdf>, Ramalho,
Ramalho and Murteira (2011) <doi:10.1111/j.1467-6419.2009.00602.x>, Fang
and Ma (2013) <doi:10.1080/02664763.2012.758246>, Mullahy (2015)
<doi:10.1515/jem-2012-0006>, Murteira and Ramalho (2016)
<doi:10.1080/07474938.2013.806849>, and Rokem and Kay (2020)
<doi:10.1093/gigascience/giaa133>.

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
