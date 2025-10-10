%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logolink
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Interface for Running 'NetLogo' Simulations

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.5
BuildRequires:    R-CRAN-checkmate >= 2.3.3
BuildRequires:    R-CRAN-janitor >= 2.2.1
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-magrittr >= 2.0.4
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-fs >= 1.6.6
BuildRequires:    R-CRAN-stringr >= 1.5.2
BuildRequires:    R-CRAN-xml2 >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.1.0
Requires:         R-CRAN-cli >= 3.6.5
Requires:         R-CRAN-checkmate >= 2.3.3
Requires:         R-CRAN-janitor >= 2.2.1
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-magrittr >= 2.0.4
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-fs >= 1.6.6
Requires:         R-CRAN-stringr >= 1.5.2
Requires:         R-CRAN-xml2 >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-purrr >= 1.1.0

%description
An interface for 'NetLogo' <https://www.netlogo.org> that enables
programmatic setup and execution of simulations. Designed to facilitate
integrating 'NetLogo' models into reproducible workflows by creating and
running 'BehaviorSpace' experiments and retrieving their results.

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
