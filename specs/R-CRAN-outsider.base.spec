%global __brp_check_rpaths %{nil}
%global packname  outsider.base
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Base Package for 'Outsider'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.1
BuildRequires:    R-CRAN-callr >= 3.0.0
BuildRequires:    R-CRAN-sys >= 2.1
BuildRequires:    R-CRAN-yaml >= 2.0
BuildRequires:    R-CRAN-devtools >= 1.1
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cli 
Requires:         R-utils >= 3.1
Requires:         R-CRAN-callr >= 3.0.0
Requires:         R-CRAN-sys >= 2.1
Requires:         R-CRAN-yaml >= 2.0
Requires:         R-CRAN-devtools >= 1.1
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-cli 

%description
Base package for 'outsider' <https://github.com/ropensci/outsider>. The
'outsider' package and its sister packages enable the installation and
running of external, command-line software within R. This base package is
a key dependency of the user-facing 'outsider' package as it provides the
utilities for interfacing between 'Docker' <https://www.docker.com> and R.
It is intended that end-users of 'outsider' do not directly work with this
base package.

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
