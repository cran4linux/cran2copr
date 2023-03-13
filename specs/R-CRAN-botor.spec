%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  botor
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          'AWS Python SDK' ('boto3') for R

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-jsonlite 

%description
Fork-safe, raw access to the 'Amazon Web Services' ('AWS') 'SDK' via the
'boto3' 'Python' module, and convenient helper functions to query the
'Simple Storage Service' ('S3') and 'Key Management Service' ('KMS'),
partial support for 'IAM', the 'Systems Manager Parameter Store' and
'Secrets Manager'.

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
