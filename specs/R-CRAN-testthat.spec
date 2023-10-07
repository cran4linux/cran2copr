%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  testthat
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unit Testing for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-processx >= 3.8.2
BuildRequires:    R-CRAN-callr >= 3.7.3
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-R6 >= 2.5.1
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.7
BuildRequires:    R-CRAN-ps >= 1.7.5
BuildRequires:    R-CRAN-desc >= 1.4.2
BuildRequires:    R-CRAN-pkgload >= 1.3.2.1
BuildRequires:    R-CRAN-brio >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-praise >= 1.0.0
BuildRequires:    R-CRAN-digest >= 0.6.33
BuildRequires:    R-CRAN-waldo >= 0.5.1
BuildRequires:    R-CRAN-ellipsis >= 0.3.2
BuildRequires:    R-CRAN-evaluate >= 0.21
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-processx >= 3.8.2
Requires:         R-CRAN-callr >= 3.7.3
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-R6 >= 2.5.1
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-jsonlite >= 1.8.7
Requires:         R-CRAN-ps >= 1.7.5
Requires:         R-CRAN-desc >= 1.4.2
Requires:         R-CRAN-pkgload >= 1.3.2.1
Requires:         R-CRAN-brio >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-praise >= 1.0.0
Requires:         R-CRAN-digest >= 0.6.33
Requires:         R-CRAN-waldo >= 0.5.1
Requires:         R-CRAN-ellipsis >= 0.3.2
Requires:         R-CRAN-evaluate >= 0.21
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
