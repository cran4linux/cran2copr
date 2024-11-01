%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FinNet
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quickly Build and Manipulate Financial Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Matrix 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
Providing classes, methods, and functions to deal with financial networks.
Users can easily store information about both physical and legal persons
by using pre-made classes that are studied for integration with scraping
packages such as 'rvest' and 'RSelenium'. Moreover, the package assists in
creating various types of financial networks depending on the type of
relation between its units depending on the relation under scrutiny
(ownership, board interlocks, etc.), the desired tie type (valued or
binary), and renders them in the most common formats (adjacency matrix,
incidence matrix, edge list, 'igraph', 'network'). There are also ad-hoc
functions for the Fiedler value, global network efficiency, and
cascade-failure analysis.

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
