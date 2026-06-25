%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ExtremeConformal
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extreme Conformal Prediction Intervals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ExtremeCI 
BuildRequires:    R-CRAN-extRemes 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-stats 
Requires:         R-CRAN-ExtremeCI 
Requires:         R-CRAN-extRemes 
Requires:         R-CRAN-ismev 
Requires:         R-stats 

%description
This new extreme conformal prediction framework provides informative
prediction intervals at the high-confidence levels for which classical
conformal methods fail. In applications with potentially high-impact
events, a very high level of confidence is often required for predictions.
If that level is too large relative to the amount of data used for
calibration, classical conformal methods provide infinitely wide, thus,
uninformative prediction intervals. Our extreme conformal procedure
bridges extreme value statistics and conformal prediction to provide
reliable and informative prediction intervals with high-confidence
coverage, which can be constructed using any black-box extreme quantile
regression method. A weighted version of the approach can account for
nonstationary data. The methodology was introduced in Pasche, Lam, and
Engelke (2026) <doi:10.1007/s10687-026-00536-9>.

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
