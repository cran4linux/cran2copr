%global packname  ccafs
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Client for 'CCAFS' 'GCM' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-jsonlite >= 1.2
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-crul >= 0.2.0
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-jsonlite >= 1.2
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-crul >= 0.2.0
Requires:         R-CRAN-httr 

%description
Client for Climate Change, Agriculture, and Food Security ('CCAFS')
General Circulation Models ('GCM') data. Data is stored in Amazon 'S3',
from which we provide functions to fetch data.

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
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX
