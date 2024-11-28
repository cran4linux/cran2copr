%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  strata
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Framework for Simple Automation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-checkmate >= 2.3.2
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-fs >= 1.6.4
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-lifecycle >= 1.0.0
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-checkmate >= 2.3.2
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-fs >= 1.6.4
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-lifecycle >= 1.0.0

%description
A tool suite for building project frameworks for users with access to only
the most basic of automation tools.

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
