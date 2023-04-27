%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jmBIG
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Longitudinal and Survival Model for Big Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-JMbayes2 
BuildRequires:    R-CRAN-joineRML 
BuildRequires:    R-CRAN-rstanarm 
BuildRequires:    R-CRAN-FastJM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-JMbayes2 
Requires:         R-CRAN-joineRML 
Requires:         R-CRAN-rstanarm 
Requires:         R-CRAN-FastJM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-survival 

%description
Provides analysis tools for big data where the sample size is very large.
It offers a suite of functions for fitting and predicting joint models,
which allow for the simultaneous analysis of longitudinal and
time-to-event data. This statistical methodology is particularly useful in
medical research where there is often interest in understanding the
relationship between a longitudinal biomarker and a clinical outcome, such
as survival or disease progression. This can be particularly useful in a
clinical setting where it is important to be able to predict how a
patient's health status may change over time. Overall, this package
provides a comprehensive set of tools for joint modeling of BIG data
obtained as survival and longitudinal outcomes with both Bayesian and
non-Bayesian approaches. Its versatility and flexibility make it a
valuable resource for researchers in many different fields,particularly in
the medical and health sciences.

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
