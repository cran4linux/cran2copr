%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  minioclient
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'MinIO' Client

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-processx 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-glue 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-processx 

%description
An R interface to the 'MinIO' Client. The 'MinIO' Client ('mc') provides a
modern alternative to UNIX commands like 'ls', 'cat', 'cp', 'mirror',
'diff', 'find' etc. It supports 'filesystems' and Amazon "S3" compatible
cloud storage service ("AWS" Signature v2 and v4). This package provides
convenience functions for installing the 'MinIO' client and running any
operations, as described in the official documentation,
<https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs-redirect>.
This package provides a flexible and high-performance alternative to
'aws.s3'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
