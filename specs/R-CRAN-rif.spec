%global packname  rif
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Client for 'Neuroscience' Information Framework 'APIs'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.3.4
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-crul >= 0.3.4
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
Client for 'Neuroscience' Information Framework ('NIF') 'APIs'
(<https://neuinfo.org/>; <https://neuinfo.org/about/webservices>). Package
includes functions for each 'API' route, and gives back data in tidy
data.frame format.

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
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
