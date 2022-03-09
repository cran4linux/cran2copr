%global __brp_check_rpaths %{nil}
%global packname  CatastRo
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the API 'Sede Electronica Del Catastro'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 1.0.0
BuildRequires:    R-CRAN-mapSpain >= 0.6.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-sf >= 1.0.0
Requires:         R-CRAN-mapSpain >= 0.6.0
Requires:         R-CRAN-rappdirs >= 0.3.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-xml2 

%description
Access public spatial data available under the 'INSPIRE' directive. Tools
for downloading references and addresses of properties, as well as map
images.

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
