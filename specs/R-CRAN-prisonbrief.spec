%global packname  prisonbrief
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Downloads and Parses World Prison Brief Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-sf >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-passport >= 0.1.1
BuildRequires:    R-CRAN-rnaturalearth >= 0.1.0
BuildRequires:    R-CRAN-rnaturalearthdata >= 0.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-sf >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-passport >= 0.1.1
Requires:         R-CRAN-rnaturalearth >= 0.1.0
Requires:         R-CRAN-rnaturalearthdata >= 0.1.0

%description
Download, parses and tidies information from the World Prison Brief
project <http://www.prisonstudies.org/>.

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
