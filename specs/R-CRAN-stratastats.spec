%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stratastats
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stratified Analysis of 2x2 Contingency Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-abind >= 1.4.0
BuildRequires:    R-CRAN-gt >= 0.8.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-abind >= 1.4.0
Requires:         R-CRAN-gt >= 0.8.0

%description
Offers a comprehensive approach for analysing stratified 2x2 contingency
tables. It facilitates the calculation of odds ratios, 95%% confidence
intervals, and conducts chi-squared tests, Cochran-Mantel-Haenszel tests,
and Breslow-Day-Tarone tests. The package is particularly useful in fields
like epidemiology and social sciences where stratified analysis is
essential. The package also provides interpretative insights into the
results, aiding in the understanding of complex statistical outcomes.

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
