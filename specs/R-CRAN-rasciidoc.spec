%global packname  rasciidoc
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Create Reports Using R and 'asciidoc'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         asciidoc
Requires:         source-highlight
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fritools >= 1.2.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-document 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-fritools >= 1.2.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-document 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-highr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-xfun 

%description
Inspired by Karl Broman`s reader on using 'knitr' with 'asciidoc'
(<http://kbroman.org/knitr_knutshell/pages/asciidoc.html>), this is merely
a wrapper to 'knitr' and 'asciidoc'.

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
