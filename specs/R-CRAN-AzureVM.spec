%global packname  AzureVM
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
