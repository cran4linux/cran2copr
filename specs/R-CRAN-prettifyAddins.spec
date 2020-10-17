%global packname  prettifyAddins
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'RStudio' Addins to Prettify 'HTML', 'CSS', 'JavaScript', and More

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
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rstudioapi 
Requires:         R-tools 
Requires:         R-CRAN-xml2 

%description
Provides 'RStudio' addins to prettify 'HTML', 'CSS', 'SCSS', 'JavaScript',
'JSX', 'Markdown', and to format 'C', 'C++', 'Julia', 'Python', 'Shell'
and 'SQL'. Two addins are provided: 'Prettify' and 'Indent'. The 'Indent'
addin only reindents the code, while the 'Prettify' addin also modifies
the code, e.g. it adds trailing semi-colons to 'JavaScript' code when they
are missing.

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
