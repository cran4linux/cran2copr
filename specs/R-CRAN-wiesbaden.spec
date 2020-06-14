%global packname  wiesbaden
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          2%{?dist}
Summary:          Access Databases from the Federal Statistical Office of Germany

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6.0
BuildRequires:    R-CRAN-stringi >= 1.4.0
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-keyring >= 1.1.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-readr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 1.6.0
Requires:         R-CRAN-stringi >= 1.4.0
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-keyring >= 1.1.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-readr >= 1.0.0

%description
Retrieve and import data from different databases of the Federal
Statistical Office of Germany (DESTATIS) using their SOAP XML web service.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
