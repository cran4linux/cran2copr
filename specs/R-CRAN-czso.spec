%global packname  czso
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Use Open Data from the Czech Statistical Office in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-tools >= 3.6.0
BuildRequires:    R-utils >= 3.6.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-usethis >= 1.5.1
BuildRequires:    R-CRAN-stringi >= 1.4.4
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-rlang >= 0.4.4
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-curl >= 4.3
Requires:         R-tools >= 3.6.0
Requires:         R-utils >= 3.6.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-usethis >= 1.5.1
Requires:         R-CRAN-stringi >= 1.4.4
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-rlang >= 0.4.4
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 

%description
Get programmatic access to the open data provided by the Czech Statistical
Office (CZSO, <https://czso.cz>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
