%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kstMatrix
%global packver   1.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Functions in Knowledge Space Theory Using Matrix Representation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-pks 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-grDevices 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-pks 

%description
Knowledge space theory by Doignon and Falmagne (1999)
<doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical framework,
which proposes mathematical formalisms to operationalize knowledge
structures in a particular domain. The 'kstMatrix' package provides basic
functionalities to generate, handle, and manipulate knowledge structures
and knowledge spaces. Opposed to the 'kst' package, 'kstMatrix' uses
matrix representations for knowledge structures. Furthermore, 'kstMatrix'
contains several knowledge spaces developed by the research group around
Cornelia Dowling through querying experts.

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
