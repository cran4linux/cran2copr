%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lbugr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to 'ladybug' Graph Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-tibble 

%description
Provides a high-performance 'R' interface to the 'ladybug' graph database.
Uses the 'reticulate' package to wrap the official Python 'ladybug'
client. Enables seamless interaction with 'Ladybug' from within 'R' for
managing database connections, executing 'Cypher' queries, and loading
data from 'R' data frames. Converts query results into popular 'R' data
structures including 'tibble', 'igraph', 'tidygraph', and 'g6R' objects
for analysis and visualization workflows.

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
