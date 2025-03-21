%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  handlr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Among Citation Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-crul 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-crul 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-yaml 

%description
Converts among many citation formats, including 'BibTeX', 'Citeproc',
'Codemeta', 'RDF XML', 'RIS', 'Schema.org', and 'Citation File Format'. A
low level 'R6' class is provided, as well as stand-alone functions for
each citation format for both read and write.

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
