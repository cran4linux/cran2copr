%global packname  spocc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to Species Occurrence Data Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-lubridate >= 1.5.0
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-rgbif >= 1.0.0
BuildRequires:    R-CRAN-rebird >= 1.0.0
BuildRequires:    R-CRAN-rvertnet >= 0.7.0
BuildRequires:    R-CRAN-rbison >= 0.6.0
BuildRequires:    R-CRAN-wicket >= 0.4.0
BuildRequires:    R-CRAN-ridigbio >= 0.3.5
BuildRequires:    R-CRAN-crul >= 0.3.4
BuildRequires:    R-CRAN-whisker >= 0.3
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-lubridate >= 1.5.0
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-rgbif >= 1.0.0
Requires:         R-CRAN-rebird >= 1.0.0
Requires:         R-CRAN-rvertnet >= 0.7.0
Requires:         R-CRAN-rbison >= 0.6.0
Requires:         R-CRAN-wicket >= 0.4.0
Requires:         R-CRAN-ridigbio >= 0.3.5
Requires:         R-CRAN-crul >= 0.3.4
Requires:         R-CRAN-whisker >= 0.3
Requires:         R-utils 

%description
A programmatic interface to many species occurrence data sources,
including Global Biodiversity Information Facility ('GBIF'), 'USGSs'
Biodiversity Information Serving Our Nation ('BISON'), 'iNaturalist',
Berkeley 'Ecoinformatics' Engine, 'eBird', Integrated Digitized
'Biocollections' ('iDigBio'), 'VertNet', Ocean 'Biogeographic' Information
System ('OBIS'), and Atlas of Living Australia ('ALA'). Includes
functionality for retrieving species occurrence data, and combining those
data.

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
