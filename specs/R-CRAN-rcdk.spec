%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcdk
%global packver   3.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the 'CDK' Libraries

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdklibs >= 2.8
BuildRequires:    R-CRAN-fingerprint 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-itertools 
Requires:         R-CRAN-rcdklibs >= 2.8
Requires:         R-CRAN-fingerprint 
Requires:         R-CRAN-rJava 
Requires:         R-methods 
Requires:         R-CRAN-png 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-itertools 

%description
Allows the user to access functionality in the 'CDK', a Java framework for
chemoinformatics. This allows the user to load molecules, evaluate
fingerprints, calculate molecular descriptors and so on. In addition, the
'CDK' API allows the user to view structures in 2D.

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
