%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wdman
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          'Webdriver'/'Selenium' Binary Manager

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-semver >= 0.2.0
BuildRequires:    R-CRAN-binman 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-utils 
Requires:         R-CRAN-semver >= 0.2.0
Requires:         R-CRAN-binman 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-yaml 
Requires:         R-utils 

%description
There are a number of binary files associated with the
'Webdriver'/'Selenium' project. This package provides functions to
download these binaries and to manage processes involving them.

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
