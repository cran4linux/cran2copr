%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chessResults
%global packver   2026.07.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2026.07.12
Release:          1%{?dist}%{?buildtag}
Summary:          Scraper for Chess-Results.com

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.3.1
BuildRequires:    R-CRAN-janitor >= 2.2.1
BuildRequires:    R-CRAN-readr >= 2.2.0
BuildRequires:    R-CRAN-stringr >= 1.6.0
BuildRequires:    R-CRAN-tidyr >= 1.3.2
BuildRequires:    R-CRAN-dplyr >= 1.2.1
BuildRequires:    R-CRAN-rvest >= 1.0.5
BuildRequires:    R-CRAN-polite >= 0.1.4
Requires:         R-CRAN-tibble >= 3.3.1
Requires:         R-CRAN-janitor >= 2.2.1
Requires:         R-CRAN-readr >= 2.2.0
Requires:         R-CRAN-stringr >= 1.6.0
Requires:         R-CRAN-tidyr >= 1.3.2
Requires:         R-CRAN-dplyr >= 1.2.1
Requires:         R-CRAN-rvest >= 1.0.5
Requires:         R-CRAN-polite >= 0.1.4

%description
Scrape data from <https://chess-results.com> and get a clean 'tibble'.
Currently supports tournament information, starting rank, playing
schedule, pairings/results for rounds, and closing rank. All requests to
the <https://chess-results.com> server are made using 'polite'.

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
