%global __brp_check_rpaths %{nil}
%global packname  starter
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Starter Kit for New Projects

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.4
BuildRequires:    R-CRAN-R.utils >= 2.11.0
BuildRequires:    R-CRAN-readr >= 2.0.1
BuildRequires:    R-CRAN-usethis >= 2.0.1
BuildRequires:    R-CRAN-fs >= 1.5.0
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-gert >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-here >= 1.0.1
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-renv >= 0.14.0
Requires:         R-CRAN-tibble >= 3.1.4
Requires:         R-CRAN-R.utils >= 2.11.0
Requires:         R-CRAN-readr >= 2.0.1
Requires:         R-CRAN-usethis >= 2.0.1
Requires:         R-CRAN-fs >= 1.5.0
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-gert >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-here >= 1.0.1
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-renv >= 0.14.0

%description
Get started with new projects by dropping a skeleton of a new project into
a new or existing directory, initialise git repositories, and create
reproducible environments with the 'renv' package. The package allows for
dynamically named files, folders, file content, as well as the
functionality to drop individual template files into existing projects.

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
