%global __brp_check_rpaths %{nil}
%global packname  GetQuandlData
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fast and Cached Import of Data from 'Quandl' Using the 'jsonAPI'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-utils 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 

%description
Imports time series data from the 'Quandl' database
<https://www.quandl.com>. The package uses the 'json api' at
<https://www.quandl.com/tools/api>, local caching ('memoise' package) and
the tidy format by default. Also allows queries of databases, allowing the
user to see which time series are available for each database id. In
short, it is an alternative to package 'Quandl', with faster data
importation in the tidy/long format.

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
