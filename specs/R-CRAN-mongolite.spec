%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mongolite
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Simple 'MongoDB' Client for R

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openssl-devel
BuildRequires:    cyrus-sasl-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-jsonlite >= 1.4
BuildRequires:    R-CRAN-openssl >= 1.0
BuildRequires:    R-CRAN-mime 
Requires:         R-CRAN-jsonlite >= 1.4
Requires:         R-CRAN-openssl >= 1.0
Requires:         R-CRAN-mime 

%description
High-performance MongoDB client based on 'mongo-c-driver' and 'jsonlite'.
Includes support for aggregation, indexing, map-reduce, streaming,
encryption, enterprise authentication, and GridFS. The online user manual
provides an overview of the available methods in the package:
<https://jeroen.github.io/mongolite/>.

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
