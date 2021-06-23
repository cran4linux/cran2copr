%global __brp_check_rpaths %{nil}
%global packname  FOCI
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Ordering by Conditional Independence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-proxy 
Requires:         R-parallel 
Requires:         R-CRAN-gmp 

%description
Feature Ordering by Conditional Independence (FOCI) is a variable
selection algorithm based on the measure of conditional dependence. For
more information, see the paper: Azadkia and Chatterjee (2019),"A simple
measure of conditional dependence" <arXiv:1910.12327>.

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
