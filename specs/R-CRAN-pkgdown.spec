%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgdown
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Make Static HTML Documentation for a Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.7.3
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-withr >= 2.4.3
BuildRequires:    R-CRAN-rmarkdown >= 2.27
BuildRequires:    R-CRAN-desc >= 1.4.0
BuildRequires:    R-CRAN-fs >= 1.4.0
BuildRequires:    R-CRAN-ragg >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-httr2 >= 1.0.2
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-bslib >= 0.5.1
BuildRequires:    R-CRAN-downlit >= 0.4.4
BuildRequires:    R-CRAN-fontawesome 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-callr >= 3.7.3
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-withr >= 2.4.3
Requires:         R-CRAN-rmarkdown >= 2.27
Requires:         R-CRAN-desc >= 1.4.0
Requires:         R-CRAN-fs >= 1.4.0
Requires:         R-CRAN-ragg >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.1
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-httr2 >= 1.0.2
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-bslib >= 0.5.1
Requires:         R-CRAN-downlit >= 0.4.4
Requires:         R-CRAN-fontawesome 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-yaml 

%description
Generate an attractive and useful website from a source package.
'pkgdown' converts your documentation, vignettes, 'README', and more to
'HTML' making it easy to share information about your package online.

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
