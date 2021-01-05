%global packname  future.BatchJobs
%global packver   0.17.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.17.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Future API for Parallel and Distributed Processing using BatchJobs

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BatchJobs >= 1.8
BuildRequires:    R-CRAN-future >= 1.21.0
BuildRequires:    R-CRAN-R.utils 
Requires:         R-CRAN-BatchJobs >= 1.8
Requires:         R-CRAN-future >= 1.21.0
Requires:         R-CRAN-R.utils 

%description
Implementation of the Future API on top of the 'BatchJobs' package. This
allows you to process futures, as defined by the 'future' package, in
parallel out of the box, not only on your local machine or ad-hoc cluster
of machines, but also via high-performance compute ('HPC') job schedulers
such as 'LSF', 'OpenLava', 'Slurm', 'SGE', and 'TORQUE' / 'PBS', e.g. 'y
<- future.apply::future_lapply(files, FUN = process)'. NOTE: The
'BatchJobs' package is deprecated in favor of the 'batchtools' package.
Because of this, it is recommended to use the 'future.batchtools' package
instead of this package.

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
