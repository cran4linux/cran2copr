%global packname  zoltr
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Interface to the 'Zoltar' Forecast Repository API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-mockery 
BuildRequires:    R-CRAN-webmockr 
BuildRequires:    R-CRAN-base64url 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MMWRweek 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-mockery 
Requires:         R-CRAN-webmockr 
Requires:         R-CRAN-base64url 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MMWRweek 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 

%description
'Zoltar' <https://www.zoltardata.com/> is a website that provides a
repository of model forecast results in a standardized format and a
central location. It supports storing, retrieving, comparing, and
analyzing time series forecasts for prediction challenges of interest to
the modeling community. This package provides functions for working with
the 'Zoltar' API, including connecting and authenticating, getting
information about projects, models, and forecasts, deleting and uploading
forecast data, and downloading scores.

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
