%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EQUALencrypt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Encryption and Decryption of Files and Data for Researchers Without Coding Skills

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-zip 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-zip 

%description
Support functions for R-based "EQUALencrypt - Encrypt and decrypt whole
files" and "EQUALencrypt - Encrypt and decrypt columns of data" shiny
applications which allow researchers without coding skills or expertise in
encryption algorithms to share data after encryption. Gurusamy,K
(2025)<doi:10.5281/zenodo.16743676> and Gurusamy,K
(2025)<doi:10.5281/zenodo.16744058>.

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
