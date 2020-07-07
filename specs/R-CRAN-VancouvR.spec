%global packname  VancouvR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Access the 'City of Vancouver' Open Data API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 

%description
Wrapper around the 'City of Vancouver' Open Data API
<https://opendata.vancouver.ca/api/v2/console> to simplify and standardize
access to 'City of Vancouver' open data. Functionality to list the data
catalogue and access data and geographic records.

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
