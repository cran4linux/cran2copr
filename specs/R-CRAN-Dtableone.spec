%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Dtableone
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tabular Comparison of Paired Diagnostic Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-epiR >= 2.0.61
BuildRequires:    R-CRAN-pROC >= 1.18.5
BuildRequires:    R-CRAN-irr >= 0.84.1
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-epiR >= 2.0.61
Requires:         R-CRAN-pROC >= 1.18.5
Requires:         R-CRAN-irr >= 0.84.1
Requires:         R-CRAN-dplyr 

%description
Offers statistical methods to compare diagnostic performance between two
binary diagnostic tests on the same subject in clinical studies. Includes
functions for generating formatted tables to display diagnostic outcomes,
facilitating a clear and comprehensive comparison directly through the R
console. Inspired by and extending the functionalities of the 'DTComPair',
'tableone', and 'gtsummary' packages.

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
