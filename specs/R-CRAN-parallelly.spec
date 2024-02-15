%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  parallelly
%global packver   1.37.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.37.0
Release:          1%{?dist}%{?buildtag}
Summary:          Enhancing the 'parallel' Package

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-parallel 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-parallel 
Requires:         R-tools 
Requires:         R-utils 

%description
Utility functions that enhance the 'parallel' package and support the
built-in parallel backends of the 'future' package.  For example,
availableCores() gives the number of CPU cores available to your R process
as given by the operating system, 'cgroups' and Linux containers, R
options, and environment variables, including those set by job schedulers
on high-performance compute clusters. If none is set, it will fall back to
parallel::detectCores(). Another example is makeClusterPSOCK(), which is
backward compatible with parallel::makePSOCKcluster() while doing a better
job in setting up remote cluster workers without the need for configuring
the firewall to do port-forwarding to your local computer.

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
