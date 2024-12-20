%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FaaSr
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          FaaS (Function as a Service) Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-paws.application.integration 
BuildRequires:    R-CRAN-paws.compute 
BuildRequires:    R-CRAN-paws.storage 
BuildRequires:    R-CRAN-paws.security.identity 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonvalidate 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-sodium 
BuildRequires:    R-CRAN-askpass 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-paws.application.integration 
Requires:         R-CRAN-paws.compute 
Requires:         R-CRAN-paws.storage 
Requires:         R-CRAN-paws.security.identity 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonvalidate 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-sodium 
Requires:         R-CRAN-askpass 

%description
Allows users to create and deploy the workflow with multiple functions in
Function-as-a-Service (FaaS) cloud computing platforms. The 'FaaSr'
package makes it simpler for R developers to use FaaS platforms by
providing the following functionality: 1) Parsing and validating a
JSON-based payload compliant to 'FaaSr' schema supporting multiple FaaS
platforms 2) Invoking user functions written in R in a Docker container
(derived from rocker), using a list generated from the parser as argument
3) Downloading/uploading of files from/to S3 buckets using simple
primitives 4) Logging to files in S3 buckets 5) Triggering downstream
actions supporting multiple FaaS platforms 6) Generating FaaS-specific API
calls to simplify the registering of a user's workflow with a FaaS
platform Supported FaaS platforms: Apache OpenWhisk
<https://openwhisk.apache.org/> GitHub Actions
<https://github.com/features/actions> Amazon Web Services (AWS) Lambda
<https://aws.amazon.com/lambda/> Supported cloud data storage for
persistent storage: Amazon Web Services (AWS) Simple Storage Service (S3)
<https://aws.amazon.com/s3/>.

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
