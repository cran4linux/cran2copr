%global packname  aqr
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Interface methods to use with an ActiveQuant Master Server

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1
Requires:         R-core >= 2.1
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RCurl 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-RCurl 

%description
This R extension provides methods to use a standalone ActiveQuant Master
Server from within R. Currently available features include fetching and
storing historical data, receiving and sending live data.  Several utility
methods for simple data transformations are included, too. For support
requests, please join the mailing list at
https://r-forge.r-project.org/mail/?group_id=1518

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
