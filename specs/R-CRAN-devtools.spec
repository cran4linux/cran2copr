%global __brp_check_rpaths %{nil}
%global packname  devtools
%global packver   2.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Make Developing R Packages Easier

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 7.2.1
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-testthat >= 3.1.4
BuildRequires:    R-CRAN-withr >= 2.5.0
BuildRequires:    R-CRAN-remotes >= 2.4.2
BuildRequires:    R-CRAN-usethis >= 2.1.6
BuildRequires:    R-CRAN-rversions >= 2.1.1
BuildRequires:    R-CRAN-pkgdown >= 2.0.6
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-fs >= 1.5.2
BuildRequires:    R-CRAN-desc >= 1.4.1
BuildRequires:    R-CRAN-rcmdcheck >= 1.4.0
BuildRequires:    R-CRAN-pkgbuild >= 1.3.1
BuildRequires:    R-CRAN-pkgload >= 1.3.0
BuildRequires:    R-CRAN-sessioninfo >= 1.2.2
BuildRequires:    R-CRAN-rlang >= 1.0.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.1
BuildRequires:    R-CRAN-urlchecker >= 1.0.1
BuildRequires:    R-CRAN-profvis >= 0.3.7
BuildRequires:    R-CRAN-ellipsis >= 0.3.2
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-roxygen2 >= 7.2.1
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-testthat >= 3.1.4
Requires:         R-CRAN-withr >= 2.5.0
Requires:         R-CRAN-remotes >= 2.4.2
Requires:         R-CRAN-usethis >= 2.1.6
Requires:         R-CRAN-rversions >= 2.1.1
Requires:         R-CRAN-pkgdown >= 2.0.6
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-fs >= 1.5.2
Requires:         R-CRAN-desc >= 1.4.1
Requires:         R-CRAN-rcmdcheck >= 1.4.0
Requires:         R-CRAN-pkgbuild >= 1.3.1
Requires:         R-CRAN-pkgload >= 1.3.0
Requires:         R-CRAN-sessioninfo >= 1.2.2
Requires:         R-CRAN-rlang >= 1.0.4
Requires:         R-CRAN-lifecycle >= 1.0.1
Requires:         R-CRAN-urlchecker >= 1.0.1
Requires:         R-CRAN-profvis >= 0.3.7
Requires:         R-CRAN-ellipsis >= 0.3.2
Requires:         R-CRAN-miniUI >= 0.1.1.1
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
