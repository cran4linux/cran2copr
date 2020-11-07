%global packname  prettifyAddins
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Addins to Prettify 'JavaScript', 'C++', 'Python', and More

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-webdriver 
BuildRequires:    R-CRAN-XRJulia 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rstudioapi 
Requires:         R-tools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-webdriver 
Requires:         R-CRAN-XRJulia 
Requires:         R-CRAN-httr 
Requires:         R-utils 

%description
Provides 'RStudio' addins to prettify 'HTML', 'CSS', 'SCSS', 'JavaScript',
'JSX', 'Markdown', 'C(++)', 'LaTeX', 'Python', 'Julia', 'XML', 'Java',
'JSON', 'Ruby', and to reindent 'C(++)', 'Fortran', 'Java', 'Julia',
'Python', 'SAS', 'Scala', 'Shell' and 'SQL'. Two kinds of addins are
provided: 'Prettify' and 'Indent'. The 'Indent' addins only reindent the
code, while the 'Prettify' addins also modify the code, e.g. trailing
semi-colons are added to 'JavaScript' code when they are missing.

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
