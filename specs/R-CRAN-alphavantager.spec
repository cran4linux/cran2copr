%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alphavantager
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight Interface to the Alpha Vantage API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-glue >= 1.1.1
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-purrr >= 0.2.2.2
BuildRequires:    R-CRAN-timetk >= 0.1.1.1
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-glue >= 1.1.1
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-purrr >= 0.2.2.2
Requires:         R-CRAN-timetk >= 0.1.1.1

%description
Alpha Vantage has free historical financial information. All you need to
do is get a free API key at <https://www.alphavantage.co>. Then you can
use the R interface to retrieve free equity information. Refer to the
Alpha Vantage website for more information.

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
