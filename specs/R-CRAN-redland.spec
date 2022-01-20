%global __brp_check_rpaths %{nil}
%global packname  redland
%global packver   1.0.17-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.17.16
Release:          1%{?dist}%{?buildtag}
Summary:          RDF Library Bindings in R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    redland-devel >= 1.0.14
BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-roxygen2 
Requires:         R-methods 
Requires:         R-CRAN-roxygen2 

%description
Provides methods to parse, query and serialize information stored in the
Resource Description Framework (RDF). RDF is described at
<https://www.w3.org/TR/rdf-primer/>. This package supports RDF by
implementing an R interface to the Redland RDF C library, described at
<https://librdf.org/docs/api/index.html>. In brief, RDF provides a
structured graph consisting of Statements composed of Subject, Predicate,
and Object Nodes.

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
