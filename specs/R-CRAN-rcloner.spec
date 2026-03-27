%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcloner
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'rclone' Cloud Storage Utility

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-utils 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-processx 
Requires:         R-utils 

%description
Provides an R interface to 'rclone' <https://rclone.org>, a command-line
program for managing files on cloud storage. 'rclone' supports over 40
cloud storage providers including 'S3'-compatible services ('Amazon S3',
'MinIO', 'Ceph'), 'Google Cloud Storage', 'Azure Blob Storage', and many
others. This package downloads and manages the 'rclone' binary
automatically and wraps its commands as R functions, returning results as
data frames where appropriate.

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
