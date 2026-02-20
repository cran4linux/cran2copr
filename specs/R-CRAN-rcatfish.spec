%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcatfish
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to the California Academy of Sciences Eschmeyer's Catalog of Fishes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 5.2.1
BuildRequires:    R-CRAN-rfishbase >= 5.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-RCurl >= 1.95.4.11
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-jsonlite >= 1.8.9
BuildRequires:    R-CRAN-httr >= 1.4.7
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-qdapRegex >= 0.7.2
BuildRequires:    R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-curl >= 5.2.1
Requires:         R-CRAN-rfishbase >= 5.0.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-RCurl >= 1.95.4.11
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-jsonlite >= 1.8.9
Requires:         R-CRAN-httr >= 1.4.7
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-qdapRegex >= 0.7.2
Requires:         R-CRAN-rvest >= 0.3.2

%description
Accesses the California Academy of Sciences Eschmeyer's Catalog of Fishes
in R using web requests. The Catalog of fishes is the leading authority in
fish taxonomy. Functions in the package allow users to search for fish
taxa and valid names, retrieve taxonomic references, retrieve monthly
taxonomic changes, obtain natural history collection information, and see
the number of species by taxonomic group. For more information on the
Catalog: Fricke, R., Eschmeyer, W. N. & R. van der Laan (eds) 2025.
ESCHMEYER'S CATALOG OF FISHES
<https://researcharchive.calacademy.org/research/ichthyology/catalog/fishcatmain.asp>.

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
