%global packname  TSCS
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Time Series Cointegrated System

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rgl >= 0.98.1
BuildRequires:    R-CRAN-tseries >= 0.10.42
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rgl >= 0.98.1
Requires:         R-CRAN-tseries >= 0.10.42
Requires:         R-stats 
Requires:         R-grDevices 

%description
A set of functions to implement Time Series Cointegrated System (TSCS)
spatial interpolation and relevant data visualization.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
