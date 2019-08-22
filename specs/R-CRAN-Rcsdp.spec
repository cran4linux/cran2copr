%global packname  Rcsdp
%global packver   0.1.55
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.55
Release:          1%{?dist}
Summary:          R Interface to the CSDP Semidefinite Programming Library

License:          CPL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
Requires:         R-methods 

%description
R interface to the CSDP semidefinite programming library. Installs version
6.1.1 of CSDP from the COIN-OR website if required. An existing
installation of CSDP may be used by passing the proper configure arguments
to the installation command. See the INSTALL file for further details.

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
%doc %{rlibdir}/%{packname}/INSTALL
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
