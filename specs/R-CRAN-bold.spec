%global packname  bold
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          Interface to Bold Systems API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-crul >= 0.3.8
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-crul >= 0.3.8
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
A programmatic interface to the Web Service methods provided by Bold
Systems (<http://www.boldsystems.org/>) for genetic 'barcode' data.
Functions include methods for searching by sequences by taxonomic names,
ids, collectors, and institutions; as well as a function for searching for
specimens, and downloading trace files.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
