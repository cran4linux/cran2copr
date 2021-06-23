%global __brp_check_rpaths %{nil}
%global packname  RWsearch
%global packver   4.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          Lazy Search in R Packages, Task Views, CRAN, the Web. All-in-One Download

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-latexpdf 
BuildRequires:    R-CRAN-networkD3 
BuildRequires:    R-CRAN-sig 
BuildRequires:    R-CRAN-sos 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-latexpdf 
Requires:         R-CRAN-networkD3 
Requires:         R-CRAN-sig 
Requires:         R-CRAN-sos 
Requires:         R-CRAN-XML 

%description
Search by keywords in R packages, task views, CRAN, the web and display
the results in the console or in txt, html or pdf files. Download the
package documentation (html index, README, NEWS, pdf manual, vignettes,
source code, binaries) with a single instruction. Visualize the package
dependencies and CRAN checks. Compare the package versions, unload and
install the packages and their dependencies in a safe order. Explore CRAN
archives. Use the above functions for task view maintenance. Access web
search engines from the console thanks to 80+ bookmarks. All functions
accept standard and non-standard evaluation.

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
