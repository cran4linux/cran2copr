%global packname  testthat
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Unit Testing for R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-callr >= 3.5.1
BuildRequires:    R-CRAN-withr >= 2.3.0
BuildRequires:    R-CRAN-cli >= 2.2.0
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-ps >= 1.3.4
BuildRequires:    R-CRAN-rlang >= 0.4.9
BuildRequires:    R-CRAN-waldo >= 0.2.4
BuildRequires:    R-CRAN-ellipsis >= 0.2.0
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-praise 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-utils 
Requires:         R-CRAN-callr >= 3.5.1
Requires:         R-CRAN-withr >= 2.3.0
Requires:         R-CRAN-cli >= 2.2.0
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-ps >= 1.3.4
Requires:         R-CRAN-rlang >= 0.4.9
Requires:         R-CRAN-waldo >= 0.2.4
Requires:         R-CRAN-ellipsis >= 0.2.0
Requires:         R-CRAN-brio 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-praise 
Requires:         R-CRAN-processx 
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
