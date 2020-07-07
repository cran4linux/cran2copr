%global packname  congressbr
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Downloads, Unpacks and Tidies Legislative Data from theBrazilian Federal Senate and Chamber of Deputies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-pscl >= 1.4.9
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-stringi >= 1.1.2
BuildRequires:    R-CRAN-janitor >= 1.1.1
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-glue >= 0.0.1
BuildRequires:    R-CRAN-progress >= 0.0.1
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-pscl >= 1.4.9
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-stringi >= 1.1.2
Requires:         R-CRAN-janitor >= 1.1.1
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-glue >= 0.0.1
Requires:         R-CRAN-progress >= 0.0.1

%description
Downloads and tidies data from the Brazilian Federal Senate and Chamber of
Deputies Application Programming Interfaces available at <http://
legis.senado.gov.br/dadosabertos/> and
<https://dadosabertos.camara.leg.br/> respectively.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
