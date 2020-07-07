%global packname  AzureVM
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}
Summary:          Virtual Machines in 'Azure'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-AzureRMR >= 2.3.0
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-AzureRMR >= 2.3.0
Requires:         R-CRAN-jsonlite 

%description
Functionality for working with virtual machines (VMs) in Microsoft's
'Azure' cloud:
<https://azure.microsoft.com/en-us/services/virtual-machines/>. Includes
facilities to deploy, startup, shutdown, and cleanly delete VMs and VM
clusters. Deployment configurations can be highly customised, and can make
use of existing resources as well as creating new ones. A selection of
predefined configurations is provided to allow easy deployment of commonly
used Linux and Windows images, including Data Science Virtual Machines.
With a running VM, execute scripts and install optional extensions. Part
of the 'AzureR' family of packages.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tpl
%{rlibdir}/%{packname}/INDEX
