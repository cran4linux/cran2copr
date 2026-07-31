%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gofmalm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for Type-II Censored Samples via the Malmquist Transformation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Goodness-of-fit tests for an arbitrary user-specified continuous
distribution under Type-II right- or left-censoring. Implements the
transformation-based method of Lin, Huang and Balakrishnan (2008)
<doi:10.1109/TR.2008.2005860>, which uses a property of order statistics
due to Malmquist (1950) to convert an r-out-of-n Type-II censored uniform
sample into a complete sample of size r, alongside the earlier
transformation of Michael and Schucany (1979)
<doi:10.1080/00401706.1979.10489813>. Also implements the direct
(untransformed) censored-sample statistics of Barr and Davidson (1973)
<doi:10.1080/00401706.1973.10489108> and Pettitt and Stephens (1976)
<doi:10.1093/biomet/63.2.291>, and the modified-statistic
maximum-likelihood procedure of Chen and Balakrishnan (1995) for testing
composite hypotheses. General background on
empirical-distribution-function goodness-of-fit methods follows D'Agostino
and Stephens (1986, ISBN:982-0-8247-7487-5).

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
