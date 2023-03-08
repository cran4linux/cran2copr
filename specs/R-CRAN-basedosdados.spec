%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  basedosdados
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Base Dos Dados' R Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.1
BuildRequires:    R-CRAN-cli >= 2.5.0
BuildRequires:    R-CRAN-dbplyr >= 2.1.1
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-fs >= 1.5.0
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-glue >= 1.4.2
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-bigrquery >= 1.4.0
BuildRequires:    R-CRAN-writexl >= 1.4.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-DBI >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-dotenv >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-typed >= 0.0.1
BuildRequires:    R-methods 
Requires:         R-CRAN-tibble >= 3.1.1
Requires:         R-CRAN-cli >= 2.5.0
Requires:         R-CRAN-dbplyr >= 2.1.1
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-fs >= 1.5.0
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-glue >= 1.4.2
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-bigrquery >= 1.4.0
Requires:         R-CRAN-writexl >= 1.4.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-DBI >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-dotenv >= 1.0.2
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-typed >= 0.0.1
Requires:         R-methods 

%description
An R interface to the 'Base dos Dados' API
<https:basedosdados.github.io/mais/py_reference_api/>). Authenticate your
project, query our tables, save data to disk and memory, all from R.

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
