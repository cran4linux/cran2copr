%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Hassani.Silva
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Test for Comparing the Predictive Accuracy of Two Sets of Forecasts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A non-parametric test founded upon the principles of the
Kolmogorov-Smirnov (KS) test, referred to as the KS Predictive Accuracy
(KSPA) test. The KSPA test is able to serve two distinct purposes.
Initially, the test seeks to determine whether there exists a
statistically significant difference between the distribution of forecast
errors, and secondly it exploits the principles of stochastic dominance to
determine whether the forecasts with the lower error also reports a
stochastically smaller error than forecasts from a competing model, and
thereby enables distinguishing between the predictive accuracy of
forecasts. KSPA test has been described in : Hassani and Silva (2015)
<doi:10.3390/econometrics3030590>.

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
