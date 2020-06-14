%global packname  readabs
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          2%{?dist}
Summary:          Download and Tidy Time Series Data from the Australian Bureau ofStatistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-hutils >= 1.5.0
BuildRequires:    R-CRAN-tibble >= 1.4.99
BuildRequires:    R-CRAN-readxl >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-rsdmx 
BuildRequires:    R-tools 
Requires:         R-CRAN-hutils >= 1.5.0
Requires:         R-CRAN-tibble >= 1.4.99
Requires:         R-CRAN-readxl >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-fst 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-rsdmx 
Requires:         R-tools 

%description
Downloads, imports, and tidies time series data from the Australian Bureau
of Statistics <https://www.abs.gov.au/>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
