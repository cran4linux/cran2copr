%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  messy.cats
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Employs String Distance Tools to Help Clean Categorical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-varhandle 
BuildRequires:    R-CRAN-rapportools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gt 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-varhandle 
Requires:         R-CRAN-rapportools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gt 

%description
Matching with string distance has never been easier! 'messy.cats' contains
various functions that employ string distance tools in order to make data
management easier for users working with categorical data. Categorical
data, especially user inputted categorical data that often tends to be
plagued by typos, can be difficult to work with. 'messy.cats' aims to
provide functions that make cleaning categorical data simple and easy.

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
