%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  senatebR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collect Data from the Brazilian Federal Senate Open Data API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.8
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-xml2 >= 1.3.6
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-jsonlite >= 1.8.8
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-xml2 >= 1.3.6
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-rvest >= 1.0.0

%description
Provides functions to access and collect data from the Brazilian Federal
Senate open data API and website. Covers senators, legislative materials,
committees, voting records, speeches, provisional measures, vetoes, and
legislative agendas, returning results as tidy data frames ready for
analysis.

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
