%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  splitpopsurv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Split-Population (Cure / Mover-Stayer) Survival Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-stats 
Requires:         R-CRAN-maxLik 
Requires:         R-stats 

%description
Maximum-likelihood estimation of split-population (cure / mover-stayer)
survival models: an accelerated failure-time regression for event timing
among "movers", combined with a logistic regression on the probability of
belonging to the immune "stayer" population. Five baseline timing
distributions are provided -- log-logistic, Weibull, log-normal, gamma,
and the generalized gamma that nests the other four -- following Schmidt &
Witte (1989, Journal of Econometrics) and Yamaguchi (1992, 1998,
Sociological Methodology). This is an R translation of a set of 'Stata' ml
programs, with the log-likelihood corrected to match the published model
and verified by simulation against known parameters.

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
