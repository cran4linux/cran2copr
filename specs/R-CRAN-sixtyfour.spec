%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sixtyfour
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Humane Interface to Amazon Web Services

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-paws >= 0.9.0
BuildRequires:    R-CRAN-paws.common >= 0.8.1
BuildRequires:    R-CRAN-s3fs >= 0.1.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-ipaddress 
Requires:         R-CRAN-paws >= 0.9.0
Requires:         R-CRAN-paws.common >= 0.8.1
Requires:         R-CRAN-s3fs >= 0.1.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-ipaddress 

%description
An opinionated interface to Amazon Web Services <https://aws.amazon.com>,
with functions for interacting with 'IAM' (Identity and Access
Management), 'S3' (Simple Storage Service), 'RDS' (Relational Data
Service), Redshift, and Billing. Lower level functions ('aws_' prefix) are
for do it yourself workflows, while higher level functions ('six_' prefix)
automate common tasks.

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
