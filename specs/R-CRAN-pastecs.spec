%global packname  pastecs
%global packver   1.3.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.21
Release:          3%{?dist}
Summary:          Package for Analysis of Space-Time Ecological Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-boot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Regularisation, decomposition and analysis of space-time series. The
pastecs R package is a PNEC-Art4 and IFREMER (Benoit Beliaeff
<Benoit.Beliaeff@ifremer.fr>) initiative to bring PASSTEC 2000
functionalities to R.

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
%doc %{rlibdir}/%{packname}/pastecs-Ex.R
%doc %{rlibdir}/%{packname}/unitTests
%{rlibdir}/%{packname}/INDEX
