%global packname  rasciidoc
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
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
BuildRequires:    R-CRAN-document 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-highr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-xfun 
Requires:         R-CRAN-document 
Requires:         R-CRAN-git2r 
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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
