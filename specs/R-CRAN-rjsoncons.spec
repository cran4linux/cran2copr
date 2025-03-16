%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rjsoncons
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Query, Pivot, Patch, and Validate 'JSON' and 'NDJSON'

License:          BSL-1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 

%description
Functions to query (filter or transform), pivot (convert from
array-of-objects to object-of-arrays, for easy import as 'R' data frame),
search, patch (edit), and validate (against 'JSON Schema') 'JSON' and
'NDJSON' strings, files, or URLs. Query and pivot support 'JSONpointer',
'JSONpath' or 'JMESpath' expressions. The implementation uses the
'jsoncons' <https://danielaparker.github.io/jsoncons/> header-only
library; the library is easily linked to other packages for direct access
to 'C++' functionality not implemented here.

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
