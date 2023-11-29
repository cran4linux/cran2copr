%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coxphw
%global packver   4.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Weighted Estimation in Cox Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Implements weighted estimation in Cox regression as proposed by Schemper,
Wakounig and Heinze (Statistics in Medicine, 2009, <doi:10.1002/sim.3623>)
and as described in Dunkler, Ploner, Schemper and Heinze (Journal of
Statistical Software, 2018, <doi:10.18637/jss.v084.i02>). Weighted Cox
regression provides unbiased average hazard ratio estimates also in case
of non-proportional hazards. Approximated generalized concordance
probability an effect size measure for clear-cut decisions can be
obtained. The package provides options to estimate time-dependent effects
conveniently by including interactions of covariates with arbitrary
functions of time, with or without making use of the weighting option.

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
