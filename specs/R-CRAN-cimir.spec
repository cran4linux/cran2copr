%global packname  cimir
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to the CIMIS Web API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 4.3
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-glue >= 1.3
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-dplyr >= 0.8
BuildRequires:    R-CRAN-rlang >= 0.4
BuildRequires:    R-CRAN-purrr >= 0.3
Requires:         R-CRAN-curl >= 4.3
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-glue >= 1.3
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-dplyr >= 0.8
Requires:         R-CRAN-rlang >= 0.4
Requires:         R-CRAN-purrr >= 0.3

%description
Connect to the California Irrigation Management Information System (CIMIS)
Web API. See the CIMIS main page <https://cimis.water.ca.gov> and web API
documentation <https://et.water.ca.gov> for more information.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
