%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  readapra
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Tidy Data from the Australian Prudential Regulation Authority

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-lubridate >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-tidyxl >= 1.0.0
BuildRequires:    R-CRAN-polite >= 0.1.0
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-ratelimitr 
BuildRequires:    R-CRAN-robotstxt 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-lubridate >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-tidyxl >= 1.0.0
Requires:         R-CRAN-polite >= 0.1.0
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-ratelimitr 
Requires:         R-CRAN-robotstxt 
Requires:         R-CRAN-stringdist 
Requires:         R-utils 

%description
Download the latest data from the Australian Prudential Regulation
Authority <https://www.apra.gov.au/> and import it into R as a tidy data
frame.

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
