%global packname  TSmisc
%global packver   2016.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2016.8.1
Release:          1%{?dist}
Summary:          'TSdbi' Extensions to Wrap Miscellaneous Data Sources

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildArch:        noarch
BuildRequires:    R-CRAN-TSdbi >= 2015.1.1
BuildRequires:    R-CRAN-quantmod >= 0.4.0
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-CRAN-tseries >= 0.10.33
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tframe 
BuildRequires:    R-CRAN-tframePlus 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-gdata 
Requires:         R-CRAN-TSdbi >= 2015.1.1
Requires:         R-CRAN-quantmod >= 0.4.0
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-CRAN-tseries >= 0.10.33
Requires:         R-methods 
Requires:         R-CRAN-tframe 
Requires:         R-CRAN-tframePlus 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-gdata 

%description
Methods to retrieve data from several different sources. This include
historical quote data from 'Yahoo' and 'Oanda', economic data from 'FRED',
and 'xls' and 'csv' data from different sources. Comprehensive examples of
all the 'TS*' packages is provided in the vignette Guide.pdf with the
'TSdata' package.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/testWithInternet
%doc %{rlibdir}/%{packname}/xlsExampleData
%{rlibdir}/%{packname}/INDEX
