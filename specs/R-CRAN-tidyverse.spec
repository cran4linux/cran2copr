%global packname  tidyverse
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Easily Install and Load the 'Tidyverse'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-lubridate >= 1.7.1
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-tibble >= 1.3.4
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-dbplyr >= 1.1.0
BuildRequires:    R-CRAN-haven >= 1.1.0
BuildRequires:    R-CRAN-cli >= 1.0.0
BuildRequires:    R-CRAN-readxl >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-tidyr >= 0.7.2
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-broom >= 0.4.2
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-hms >= 0.3
BuildRequires:    R-CRAN-purrr >= 0.2.4
BuildRequires:    R-CRAN-forcats >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.1.4
BuildRequires:    R-CRAN-modelr >= 0.1.1
BuildRequires:    R-CRAN-reprex >= 0.1.1
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-lubridate >= 1.7.1
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-tibble >= 1.3.4
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-dbplyr >= 1.1.0
Requires:         R-CRAN-haven >= 1.1.0
Requires:         R-CRAN-cli >= 1.0.0
Requires:         R-CRAN-readxl >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-tidyr >= 0.7.2
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-broom >= 0.4.2
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-hms >= 0.3
Requires:         R-CRAN-purrr >= 0.2.4
Requires:         R-CRAN-forcats >= 0.2.0
Requires:         R-CRAN-rlang >= 0.1.4
Requires:         R-CRAN-modelr >= 0.1.1
Requires:         R-CRAN-reprex >= 0.1.1

%description
The 'tidyverse' is a set of packages that work in harmony because they
share common data representations and 'API' design. This package is
designed to make it easy to install and load multiple 'tidyverse' packages
in a single step. Learn more about the 'tidyverse' at
<https://tidyverse.org>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
