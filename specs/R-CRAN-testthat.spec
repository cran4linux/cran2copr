%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  testthat
%global packver   3.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unit Testing for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-processx >= 3.8.6
BuildRequires:    R-CRAN-callr >= 3.7.6
BuildRequires:    R-CRAN-cli >= 3.6.5
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-R6 >= 2.6.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 2.0.0
BuildRequires:    R-CRAN-ps >= 1.9.1
BuildRequires:    R-CRAN-desc >= 1.4.3
BuildRequires:    R-CRAN-pkgload >= 1.4.0
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-brio >= 1.1.5
BuildRequires:    R-CRAN-evaluate >= 1.0.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-praise >= 1.0.0
BuildRequires:    R-CRAN-waldo >= 0.6.2
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.8.6
Requires:         R-CRAN-callr >= 3.7.6
Requires:         R-CRAN-cli >= 3.6.5
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-R6 >= 2.6.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-jsonlite >= 2.0.0
Requires:         R-CRAN-ps >= 1.9.1
Requires:         R-CRAN-desc >= 1.4.3
Requires:         R-CRAN-pkgload >= 1.4.0
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-brio >= 1.1.5
Requires:         R-CRAN-evaluate >= 1.0.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-praise >= 1.0.0
Requires:         R-CRAN-waldo >= 0.6.2
Requires:         R-methods 
Requires:         R-utils 

%description
Software testing is important, but, in part because it is frustrating and
boring, many of us avoid it. 'testthat' is a testing framework for R that
is easy to learn and use, and integrates with your existing 'workflow'.

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
