%global packname  BARIS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Access and Import Data from the French Open Data Portal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98.1.20
BuildRequires:    R-utils >= 3.6.1
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-rgdal >= 1.4.4
BuildRequires:    R-CRAN-stringi >= 1.4.3
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-janitor >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-memoise >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-sf >= 0.7.7
BuildRequires:    R-CRAN-rio >= 0.5.16
BuildRequires:    R-CRAN-downloader >= 0.4
Requires:         R-CRAN-XML >= 3.98.1.20
Requires:         R-utils >= 3.6.1
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-rgdal >= 1.4.4
Requires:         R-CRAN-stringi >= 1.4.3
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-janitor >= 1.2.0
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-memoise >= 1.1.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-sf >= 0.7.7
Requires:         R-CRAN-rio >= 0.5.16
Requires:         R-CRAN-downloader >= 0.4

%description
Allows the user to access and import data from the rich French open data
portal through the provided free API
<https://doc.data.gouv.fr/api/reference/>. The portal is free, and no
credential is required for extracting datasets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
