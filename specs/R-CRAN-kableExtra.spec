%global packname  kableExtra
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Complex Table with 'kable' and Pipe Syntax

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.6
BuildRequires:    R-CRAN-knitr >= 1.16
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-graphics 
Requires:         R-CRAN-rmarkdown >= 1.6
Requires:         R-CRAN-knitr >= 1.16
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridisLite 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-glue 
Requires:         R-tools 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-digest 
Requires:         R-graphics 

%description
Build complex HTML or 'LaTeX' tables using 'kable()' from 'knitr' and the
piping syntax from 'magrittr'. Function 'kable()' is a light weight table
generator coming from 'knitr'. This package simplifies the way to
manipulate the HTML or 'LaTeX' codes generated by 'kable()' and allows
users to construct complex tables and customize styles using a readable
syntax.

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
