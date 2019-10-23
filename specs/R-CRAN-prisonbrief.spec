%global packname  prisonbrief
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Downloads and Parses World Prison Brief Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.3.3
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-tidyr >= 0.6.3
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
BuildRequires:    R-CRAN-rlang >= 0.1.1
BuildRequires:    R-CRAN-passport >= 0.1.1
BuildRequires:    R-CRAN-rnaturalearth >= 0.1.0
BuildRequires:    R-CRAN-rnaturalearthdata >= 0.1.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.3.3
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-tidyr >= 0.6.3
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-rlang >= 0.1.1
Requires:         R-CRAN-passport >= 0.1.1
Requires:         R-CRAN-rnaturalearth >= 0.1.0
Requires:         R-CRAN-rnaturalearthdata >= 0.1.0

%description
Download, parses and tidies information from the World Prison Brief
project <http://www.prisonstudies.org/>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
