%global __brp_check_rpaths %{nil}
%global packname  RstoxData
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Read and Manipulate Fisheries Data

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-stringi >= 1.4.3
BuildRequires:    R-CRAN-xslt >= 1.4
BuildRequires:    R-CRAN-xml2 >= 1.2.2
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-units >= 0.7
Requires:         R-CRAN-stringi >= 1.4.3
Requires:         R-CRAN-xslt >= 1.4
Requires:         R-CRAN-xml2 >= 1.2.2
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-units >= 0.7

%description
Set of tools to read and manipulate various data formats for fisheries.
Mainly catered towards scientific trawl survey sampling ('biotic') data,
acoustic trawl data, and commercial fishing catch ('landings') data. Among
the supported data formats are the data products from the Norwegian
Institute Marine Research ('IMR') and the International Council for the
Exploration of the Sea (ICES).

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
