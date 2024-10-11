%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autometric
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Background Resource Logging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-utils 

%description
Intense parallel workloads can be difficult to monitor. Packages
'crew.cluster', 'clustermq', and 'future.batchtools' distribute hundreds
of worker processes over multiple computers. If a worker process exhausts
its available memory, it may terminate silently, leaving the underlying
problem difficult to detect or troubleshoot. Using the 'autometric'
package, a worker can proactively monitor itself in a detached background
thread. The worker process itself runs normally, and the thread writes to
a log every few seconds. If the worker terminates unexpectedly,
'autometric' can read and visualize the log file to reveal potential
resource-related reasons for the crash. The 'autometric' package borrows
heavily from the methods of packages 'ps' <doi:10.32614/CRAN.package.ps>
and 'psutil'.

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
