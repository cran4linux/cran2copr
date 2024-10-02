%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  timeROC
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Dependent ROC Curve and AUC for Censored Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.1
Requires:         R-core >= 2.9.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pec >= 2.4.4
BuildRequires:    R-CRAN-mvtnorm >= 1.0.1
Requires:         R-CRAN-pec >= 2.4.4
Requires:         R-CRAN-mvtnorm >= 1.0.1

%description
Estimation of time-dependent ROC curve and area under time dependent ROC
curve (AUC) in the presence of censored data, with or without competing
risks. Confidence intervals of AUCs and tests for comparing AUCs of two
rival markers measured on the same subjects can be computed, using the
iid-representation of the AUC estimator. Plot functions for time-dependent
ROC curves and AUC curves are provided. Time-dependent Positive Predictive
Values (PPV) and Negative Predictive Values (NPV) can also be computed.
See Blanche et al. (2013) <doi:10.1002/sim.5958> and references therein
for the details of the methods implemented in the package.

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
