%global packname  individual
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for Specifying and Simulating Individual Based Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-testthat 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 

%description
A framework which provides users a set of useful primitive elements for
specifying individual based simulation models, with special attention
models for infectious disease epidemiology. Users build models by
specifying variables for each characteristic of individuals in the
simulated population by using data structures exposed by the package. The
package provides efficient methods for finding subsets of individuals
based on these variables, or cohorts. Cohorts can then be targeted for
variable updates or scheduled for events. Variable updates queued during a
time step are executed at the end of a discrete time step, and the code
places no restrictions on how individuals are allowed to interact. These
data structures are designed to provide an intuitive way for users to turn
their conceptual model of a system into executable code, which is fast and
memory efficient.

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
