%global packname  devtools
%global packver   2.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Make Developing R Packages Easier

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 7.1.1
BuildRequires:    R-CRAN-callr >= 3.6.0
BuildRequires:    R-CRAN-testthat >= 3.0.2
BuildRequires:    R-CRAN-withr >= 2.4.1
BuildRequires:    R-CRAN-cli >= 2.4.0
BuildRequires:    R-CRAN-remotes >= 2.3.0
BuildRequires:    R-CRAN-rversions >= 2.0.2
BuildRequires:    R-CRAN-usethis >= 2.0.1
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-fs >= 1.5.0
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-rcmdcheck >= 1.3.3
BuildRequires:    R-CRAN-desc >= 1.3.0
BuildRequires:    R-CRAN-pkgload >= 1.2.1
BuildRequires:    R-CRAN-pkgbuild >= 1.2.0
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-ellipsis >= 0.3.1
BuildRequires:    R-CRAN-rstudioapi >= 0.13
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-roxygen2 >= 7.1.1
Requires:         R-CRAN-callr >= 3.6.0
Requires:         R-CRAN-testthat >= 3.0.2
Requires:         R-CRAN-withr >= 2.4.1
Requires:         R-CRAN-cli >= 2.4.0
Requires:         R-CRAN-remotes >= 2.3.0
Requires:         R-CRAN-rversions >= 2.0.2
Requires:         R-CRAN-usethis >= 2.0.1
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-fs >= 1.5.0
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-rcmdcheck >= 1.3.3
Requires:         R-CRAN-desc >= 1.3.0
Requires:         R-CRAN-pkgload >= 1.2.1
Requires:         R-CRAN-pkgbuild >= 1.2.0
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-ellipsis >= 0.3.1
Requires:         R-CRAN-rstudioapi >= 0.13
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Collection of package development tools.

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
