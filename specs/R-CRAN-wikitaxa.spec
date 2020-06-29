%global packname  wikitaxa
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Taxonomic Information from 'Wikipedia'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.3.4
BuildRequires:    R-CRAN-WikidataR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-crul >= 0.3.4
Requires:         R-CRAN-WikidataR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 

%description
'Taxonomic' information from 'Wikipedia', 'Wikicommons', 'Wikispecies',
and 'Wikidata'. Functions included for getting taxonomic information from
each of the sources just listed, as well performing taxonomic search.

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
