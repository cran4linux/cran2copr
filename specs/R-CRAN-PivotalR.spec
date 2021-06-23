%global __brp_check_rpaths %{nil}
%global packname  PivotalR
%global packver   0.1.18.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18.5
Release:          1%{?dist}%{?buildtag}
Summary:          A Fast, Easy-to-Use Tool for Manipulating Tables in Databases and a Wrapper of MADlib

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-semver 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-semver 

%description
Provides an R interface for the 'VMware Data Stack' running on
'PostgreSQL' or 'Greenplum' databases with parallel and distributed
computation ability for big data processing. 'PivotalR' provides an R
interface to various database operations on tables or views. These
operations are almost the same as the corresponding native R operations.
Thus users of R do not need to learn 'SQL' when they operate on objects in
the database. It also provides a wrapper for 'Apache MADlib', which is an
open-source library for parallel and scalable in-database analytics.

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
