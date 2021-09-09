%global __brp_check_rpaths %{nil}
%global packname  recapr
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Two Event Mark-Recapture Experiment

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Tools are provided for estimating, testing, and simulating abundance in a
two-event (Petersen) mark-recapture experiment. Functions are given to
calculate the Petersen, Chapman, and Bailey estimators and associated
variances. However, the principal utility is a set of functions to
simulate random draws from these estimators, and use these to conduct
hypothesis tests and power calculations. Additionally, a set of functions
are provided for generating confidence intervals via bootstrapping.
Functions are also provided to test abundance estimator consistency under
complete or partial stratification, and to calculate stratified or
partially stratified estimators. Functions are also provided to calculate
recommended sample sizes. Referenced methods can be found in Arnason et
al. (1996) <ISSN:0706-6457>, Bailey (1951) <DOI:10.2307/2332575>, Bailey
(1952) <DOI:10.2307/1913>, Chapman (1951) NAID:20001644490, Cohen (1988)
ISBN:0-12-179060-6, Darroch (1961) <DOI:10.2307/2332748>, and Robson and
Regier (1964) <ISSN:1548-8659>.

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
