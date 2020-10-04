%global packname  worrms
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}%{?buildtag}
Summary:          World Register of Marine Species (WoRMS) Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crul >= 0.6.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crul >= 0.6.0
Requires:         R-CRAN-data.table 

%description
Client for World Register of Marine Species
(<http://www.marinespecies.org/>). Includes functions for each of the API
methods, including searching for names by name, date and common names,
searching using external identifiers, fetching synonyms, as well as
fetching taxonomic children and taxonomic classification.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
