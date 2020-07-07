%global packname  traits
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Species Trait Data from Around the Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 0.9
BuildRequires:    R-CRAN-taxize >= 0.7.4
BuildRequires:    R-CRAN-crul >= 0.6.0
BuildRequires:    R-CRAN-rvest >= 0.3.1
BuildRequires:    R-CRAN-xml2 >= 0.1.2
BuildRequires:    R-CRAN-hoardr 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite >= 0.9
Requires:         R-CRAN-taxize >= 0.7.4
Requires:         R-CRAN-crul >= 0.6.0
Requires:         R-CRAN-rvest >= 0.3.1
Requires:         R-CRAN-xml2 >= 0.1.2
Requires:         R-CRAN-hoardr 

%description
Species trait data from many different sources, including sequence data
from 'NCBI', plant trait data from 'BETYdb', plant data from the USDA
plants database, data from 'EOL' 'Traitbank', Coral traits data
(<https://coraltraits.org>), 'Birdlife' International, and more.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/PLANTATT_19_Nov_08
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
