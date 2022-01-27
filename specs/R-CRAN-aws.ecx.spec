%global __brp_check_rpaths %{nil}
%global packname  aws.ecx
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Communicating with AWS EC2 and ECS using AWS REST APIs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-aws.signature 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-aws.signature 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-utils 

%description
Providing the functions for communicating with Amazon Web Services(AWS)
Elastic Compute Cloud(EC2) and Elastic Container Service(ECS). The
functions will have the prefix 'ecs_' or 'ec2_' depending on the class of
the API. The request will be sent via the REST API and the parameters are
given by the function argument. The credentials can be set via
'aws_set_credentials'. The EC2 documentation can be found at
<https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html> and
ECS can be found at
<https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html>.

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
