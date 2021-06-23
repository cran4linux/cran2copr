%global __brp_check_rpaths %{nil}
%global packname  cmdfun
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for Building Interfaces to Shell Commands

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-usethis 
Requires:         R-utils 

%description
Writing interfaces to command line software is cumbersome. 'cmdfun'
provides a framework for building function calls to seamlessly interface
with shell commands by allowing lazy evaluation of command line arguments.
'cmdfun' also provides methods for handling user-specific paths to tool
installs or secrets like API keys. Its focus is to equally serve package
builders who wish to wrap command line software, and to help analysts stay
inside R when they might usually leave to execute non-R software.

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
