%global packname  nowcasting
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}
Summary:          Predicting Economic Variables using Dynamic Factor Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-RMySQL 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-stats 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-RMySQL 
Requires:         R-Matrix 
Requires:         R-CRAN-vars 
Requires:         R-stats 

%description
It contains the tools to implement dynamic factor models to forecast
economic variables. The user will be able to construct pseudo real time
vintages, use information criteria for determining the number of factors
and shocks, estimate the model, and visualize results among other things.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
