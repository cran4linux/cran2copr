%global __brp_check_rpaths %{nil}
%global packname  PP
%global packver   0.6.3-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Person Parameter Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
The PP package includes estimation of (MLE, WLE, MAP, EAP, ROBUST) person
parameters for the 1,2,3,4-PL model and the GPCM (generalized partial
credit model). The parameters are estimated under the assumption that the
item parameters are known and fixed. The package is useful e.g. in the
case that items from an item pool / item bank with known item parameters
are administered to a new population of test-takers and an ability
estimation for every test-taker is needed.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
