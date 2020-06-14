%global packname  FSK2R
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          An Interface Between the 'FSK-ML' Standard and 'R'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.98
BuildRequires:    R-tools >= 3.5.3
BuildRequires:    R-utils >= 3.5.3
BuildRequires:    R-CRAN-R.utils >= 2.9.0
BuildRequires:    R-CRAN-zip >= 2.0.4
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-readtext >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-googlesheets >= 0.3.0
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-rjson >= 0.2.20
Requires:         R-CRAN-XML >= 3.98
Requires:         R-tools >= 3.5.3
Requires:         R-utils >= 3.5.3
Requires:         R-CRAN-R.utils >= 2.9.0
Requires:         R-CRAN-zip >= 2.0.4
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-readtext >= 0.7
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-googlesheets >= 0.3.0
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-rjson >= 0.2.20

%description
Functions for importing, creating, editing and exporting 'FSK' files
<https://foodrisklabs.bfr.bund.de/fsk-ml-food-safety-knowledge-markup-language/>
using the 'R' programming environment. Furthermore, it enables users to
run simulations contained in the 'FSK' files and visualize the results.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
