%global __brp_check_rpaths %{nil}
%global packname  AzureContainers
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'Container Instances', 'Docker Registry' and 'Kubernetes' in 'Azure'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureRMR >= 2.0.0
BuildRequires:    R-CRAN-AzureGraph >= 1.1.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-processx 
Requires:         R-CRAN-AzureRMR >= 2.0.0
Requires:         R-CRAN-AzureGraph >= 1.1.0
Requires:         R-utils 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-processx 

%description
An interface to container functionality in Microsoft's 'Azure' cloud:
<https://azure.microsoft.com/en-us/product-categories/containers/>. Manage
'Azure Container Instance' (ACI), 'Azure Container Registry' (ACR) and
'Azure Kubernetes Service' (AKS) resources, push and pull images, and
deploy services. On the client side, lightweight shells to the 'docker',
'docker-compose', 'kubectl' and 'helm' commandline tools are provided.
Part of the 'AzureR' family of packages.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
