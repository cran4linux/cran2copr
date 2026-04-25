%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vivaglint
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis Tools for 'Viva Glint' Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.7.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-readr >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.7.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0

%description
Provides functions for importing, validating, and analyzing 'Viva Glint'
survey data exports, with optional API-based import via the 'Microsoft
Graph' API. Includes tools for data reshaping, question-level analysis,
multi-cycle comparisons, organizational hierarchy analysis, factor
analysis, and correlation analysis. Harman (1960, ISBN: 0226316513);
Husser (2017) <doi:10.1002/9781118901731.iecrm0048>.

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
