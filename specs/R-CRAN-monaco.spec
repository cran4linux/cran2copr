%global packname  monaco
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          The 'Monaco' Editor as a HTML Widget

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-rstudioapi 
Requires:         R-tools 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-shiny 

%description
A HTML widget rendering the 'Monaco' editor. The 'Monaco' editor is the
code editor which powers 'VS Code'. It is particularly well developed for
'JavaScript'. In addition to the built-in features of the 'Monaco' editor,
the widget allows to prettify multiple languages, to view the 'HTML'
rendering of 'Markdown' code, and to view and resize 'SVG' images.

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
