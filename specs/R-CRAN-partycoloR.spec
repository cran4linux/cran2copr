%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  partycoloR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Party Colors and Logos from Wikipedia

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-xml2 >= 1.3.0
BuildRequires:    R-CRAN-rvest >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.3.0
Requires:         R-CRAN-curl >= 4.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-xml2 >= 1.3.0
Requires:         R-CRAN-rvest >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr >= 0.3.0

%description
Extract political party colors and logos from English Wikipedia party
pages. Provides functions to scrape party infoboxes for color codes (HEX
or HTML color names) and logo images. Includes integration with the Party
Facts database for easy party lookups. Designed for political scientists
and party researchers working with electoral and party data. For Party
Facts, see Döring and Regel (2019) <doi:10.1177/1354068818820671> and
Bederke, Döring, and Regel (2023) <doi:10.7910/DVN/TJINLQ>.

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
