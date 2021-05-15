%global packname  hydroscoper
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Greek National Data Bank for Hydrometeorological Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1
BuildRequires:    R-CRAN-pingr >= 2.0
BuildRequires:    R-CRAN-jsonlite >= 1.7
BuildRequires:    R-CRAN-stringi >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-readr >= 1.4
Requires:         R-CRAN-tibble >= 3.1
Requires:         R-CRAN-pingr >= 2.0
Requires:         R-CRAN-jsonlite >= 1.7
Requires:         R-CRAN-stringi >= 1.5
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-readr >= 1.4

%description
R interface to the Greek National Data Bank for Hydrological and
Meteorological Information. It covers Hydroscope's data sources and
provides functions to transliterate, translate and download them into tidy
dataframes.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
