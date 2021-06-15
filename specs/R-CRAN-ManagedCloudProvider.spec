%global packname  ManagedCloudProvider
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Providing the Kubernetes-Like Functions for the Non-Kubernetes Cloud Service

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DockerParallel >= 1.0.3
BuildRequires:    R-CRAN-adagio 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-DockerParallel >= 1.0.3
Requires:         R-CRAN-adagio 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 

%description
Providing the kubernetes-like class 'ManagedCloudProvider' as a child
class of the 'CloudProvider' class in the 'DockerParallel' package. The
class is able to manage the cloud instance made by the non-kubernetes
cloud service. For creating a provider for the non-kubernetes cloud
service, the developer needs to define a reference class inherited from
'ManagedCloudProvider' and define the method for the generics
runDockerWorkerContainers(), getDockerWorkerStatus() and
killDockerWorkerContainers(). For more information, please see the
vignette in this package and
<https://CRAN.R-project.org/package=DockerParallel>.

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
