%global __brp_check_rpaths %{nil}
%global packname  rlist
%global packver   0.4.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Non-Tabular Data Manipulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-data.table 

%description
Provides a set of functions for data manipulation with list objects,
including mapping, filtering, grouping, sorting, updating, searching, and
other useful functions. Most functions are designed to be pipeline
friendly so that data processing with lists can be chained.

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
