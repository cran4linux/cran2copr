%global packname  kofdata
%global packver   0.1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.3
Release:          1%{?dist}
Summary:          Get Data from the 'KOF Datenservice' API

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Read Swiss time series data from the 'KOF Datenservice' API,
<https://datenservice.kof.ethz.ch>. The API provides macroeconomic survey
data, business cycle and further macro economic time series about
Switzerland. The package itself is a set of wrappers around the 'KOF
Datenservice' API. The 'kofdata' package is able to consume public
information as well as data that requires an API token.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
