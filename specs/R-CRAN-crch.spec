%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crch
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Censored Regression with Conditional Heteroscedasticity

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-scoringRules 
Requires:         R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-scoringRules 

%description
Different approaches to censored or truncated regression with conditional
heteroscedasticity are provided. First, continuous distributions can be
used for the (right and/or left censored or truncated) response with
separate linear predictors for the mean and variance. Second, cumulative
link models for ordinal data (obtained by interval-censoring continuous
data) can be employed for heteroscedastic extended logistic regression
(HXLR). In the latter type of models, the intercepts depend on the
thresholds that define the intervals. Infrastructure for working with
censored or truncated normal, logistic, and Student-t distributions, i.e.,
d/p/q/r functions and distributions3 objects.

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
