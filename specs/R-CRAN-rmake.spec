%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmake
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Makefile Generator for R Analytical Projects

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-knitr 
Requires:         R-tools 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-knitr 

%description
Creates and maintains a build process for complex analytic tasks in R.
Package allows to easily generate Makefile for the (GNU) 'make' tool,
which drives the build process by (in parallel) executing build commands
in order to update results accordingly to given dependencies on changed
data or updated source files.

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
