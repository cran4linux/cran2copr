%global __brp_check_rpaths %{nil}
%global packname  atom4R
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Handle and Publish Metadata as 'Atom' XML Format

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-zip 
BuildRequires:    R-CRAN-rdflib 
BuildRequires:    R-CRAN-keyring 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-zip 
Requires:         R-CRAN-rdflib 
Requires:         R-CRAN-keyring 

%description
Provides tools to read/write/publish metadata based on the 'Atom' XML
syndication format. This includes support of 'Dublin Core' XML
implementation, and a client to API(s) implementing the 'AtomPub' 'SWORD'
API specification.

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
