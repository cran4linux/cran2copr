%global packname  snow
%global packver   0.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Simple Network of Workstations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.1
Requires:         R-core >= 2.13.1
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Support for simple parallel computing in R.

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
%doc %{rlibdir}/%{packname}/RMPInode.R
%doc %{rlibdir}/%{packname}/RMPInode.sh
%doc %{rlibdir}/%{packname}/RMPISNOW
%doc %{rlibdir}/%{packname}/RMPISNOWprofile
%doc %{rlibdir}/%{packname}/RNWSnode.R
%doc %{rlibdir}/%{packname}/RNWSnode.sh
%doc %{rlibdir}/%{packname}/RPVMnode.R
%doc %{rlibdir}/%{packname}/RPVMnode.sh
%doc %{rlibdir}/%{packname}/RSOCKnode.R
%doc %{rlibdir}/%{packname}/RSOCKnode.sh
%doc %{rlibdir}/%{packname}/RunSnowNode
%doc %{rlibdir}/%{packname}/RunSnowWorker
%doc %{rlibdir}/%{packname}/RunSnowWorker.bat
%{rlibdir}/%{packname}/INDEX
