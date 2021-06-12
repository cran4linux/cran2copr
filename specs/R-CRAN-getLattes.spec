%global packname  getLattes
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Import and Process Data from the 'Lattes' Curriculum Platform

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-pipeR 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-pipeR 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-purrr 

%description
Tool for import and process data from 'Lattes' curriculum platform
(<http://lattes.cnpq.br/>). The Brazilian government keeps an extensive
base of curricula for academics from all over the country, with over 5
million registrations. The academic life of the Brazilian researcher, or
related to Brazilian universities, is documented in 'Lattes'. Some
information that can be obtained: professional formation, research area,
publications, academics advisories, projects, etc. 'getLattes' package
allows work with 'Lattes' data exported to XML format.

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
