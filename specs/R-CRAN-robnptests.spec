%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robnptests
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Nonparametric Two-Sample Tests for Location/Scale

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-checkmate 

%description
Implementations of several robust nonparametric two-sample tests for
location or scale differences. The test statistics are based on robust
location and scale estimators, e.g. the sample median or the
Hodges-Lehmann estimators as described in Fried & Dehling (2011)
<doi:10.1007/s10260-011-0164-1>. The p-values can be computed via the
permutation principle, the randomization principle, or by using the
asymptotic distributions of the test statistics under the null hypothesis,
which ensures (approximate) distribution independence of the test
decision. To test for a difference in scale, we apply the tests for
location difference to transformed observations; see Fried (2012)
<doi:10.1016/j.csda.2011.02.012>. Random noise on a small range can be
added to the original observations in order to hold the significance level
on data from discrete distributions. The location tests assume
homoscedasticity and the scale tests require the location parameters to be
zero.

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
