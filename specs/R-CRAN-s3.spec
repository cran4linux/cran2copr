%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  s3
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download Files from 'AWS S3'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-cli 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-dplyr 

%description
Download files hosted on 'AWS S3' (Amazon Web Services Simple Storage
Service; <https://aws.amazon.com/s3/>) to a local directory based on their
URI. Avoid downloading files that are already present locally.  Allow for
customization of where to store downloaded files.

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
