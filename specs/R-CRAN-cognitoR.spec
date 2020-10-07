%global packname  cognitoR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Authentication for 'Shiny' Apps with 'Amazon Cognito'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-paws 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-config 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-paws 

%description
Provides authentication for Shiny applications using 'Amazon Cognito' (
<https://aws.amazon.com/es/cognito/>).

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
