%global __brp_check_rpaths %{nil}
%global packname  googleCloudStorageR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interface with Google Cloud Storage API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.0.3
BuildRequires:    R-CRAN-googleAuthR >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-zip >= 2.0.3
Requires:         R-CRAN-googleAuthR >= 1.3.1
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-curl 
Requires:         R-CRAN-openssl 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Interact with Google Cloud Storage <https://cloud.google.com/storage/> API
in R. Part of the 'cloudyr' <https://cloudyr.github.io/> project.

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
