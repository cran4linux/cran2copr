%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rgof
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          1d Goodness of Fit Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-microbenchmark 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-microbenchmark 

%description
Routines that allow the user to run a large number of goodness-of-fit
tests. It allows for data to be continuous or discrete. It includes
routines to estimate the power of the tests and display them as a power
graph. The routine run.studies allows a user to quickly study the power of
a new method and how it compares to some of the standard ones.

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
