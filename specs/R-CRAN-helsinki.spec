%global packname  helsinki
%global packver   0.9.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.29
Release:          3%{?dist}
Summary:          R Tools for Helsinki Open Data

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-sp 

%description
Tools for accessing various open data sources in the Helsinki region in
Finland. Current data sources include the Real Estate Department
(<http://ptp.hel.fi/avoindata/>), Service Map API
(<http://api.hel.fi/servicemap/v1/>), Linked Events API
(<http://api.hel.fi/linkedevents/v0.1/>), Helsinki Region Infoshare
statistics API (<https://dev.hel.fi/stats/>).

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
