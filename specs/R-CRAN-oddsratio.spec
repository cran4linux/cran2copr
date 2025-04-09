%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oddsratio
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Odds Ratio Calculation for GAM(M)s & GLM(M)s

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-mgcv 
Requires:         R-stats 

%description
Simplified odds ratio calculation of GAM(M)s & GLM(M)s. Provides
structured output (data frame) of all predictors and their corresponding
odds ratios and confident intervals for further analyses.  It helps to
avoid false references of predictors and increments by specifying these
parameters in a list instead of using 'exp(coef(model))' (standard
approach of odds ratio calculation for GLMs) which just returns a plain
numeric output.  For GAM(M)s, odds ratio calculation is highly simplified
with this package since it takes care of the multiple 'predict()' calls of
the chosen predictor while holding other predictors constant. Also, this
package allows odds ratio calculation of percentage steps across the whole
predictor distribution range for GAM(M)s.  In both cases, confident
intervals are returned additionally. Calculated odds ratio of GAM(M)s can
be inserted into the smooth function plot.

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
