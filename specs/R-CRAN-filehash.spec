%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  filehash
%global packver   2.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.6
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Key-Value Database

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-methods 
Requires:         R-CRAN-digest 
Requires:         R-methods 

%description
Implements a simple key-value style database where character string keys
are associated with data values that are stored on the disk. A simple
interface is provided for inserting, retrieving, and deleting data from
the database. Utilities are provided that allow 'filehash' databases to be
treated much like environments and lists are already used in R. These
utilities are provided to encourage interactive and exploratory analysis
on large datasets. Three different file formats for representing the
database are currently available and new formats can easily be
incorporated by third parties for use in the 'filehash' framework.

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
