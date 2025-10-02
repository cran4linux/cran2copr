%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExtendedABSurvTDC
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis using Indicators under Time Dependent Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-readxl 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-readxl 

%description
Survival analysis is employed to model time-to-event data. This package
examines the relationship between survival and one or more predictors,
termed as covariates, which can include both treatment variables (e.g.,
season of birth, represented by indicator functions) and continuous
variables. To this end, the Cox-proportional hazard (Cox-PH) model,
introduced by Cox in 1972, is a widely applicable and commonly used method
for survival analysis. This package enables the estimation of the effect
of randomization for the treatment variable to account for potential
confounders, providing adjustment when estimating the association with
exposure. It accommodates both fixed and time-dependent covariates and
computes survival probabilities for lactation periods in dairy animals.
The package is built upon the algorithm developed by Klein and
Moeschberger (2003) <DOI:10.1007/b97377>.

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
