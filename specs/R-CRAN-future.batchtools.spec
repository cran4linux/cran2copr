%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  future.batchtools
%global packver   0.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Future API for Parallel and Distributed Processing using 'batchtools'

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.31.0
BuildRequires:    R-CRAN-batchtools >= 0.9.13
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.31.0
Requires:         R-CRAN-batchtools >= 0.9.13
Requires:         R-CRAN-parallelly 
Requires:         R-utils 

%description
Implementation of the Future API on top of the 'batchtools' package. This
allows you to process futures, as defined by the 'future' package, in
parallel out of the box, not only on your local machine or ad-hoc cluster
of machines, but also via high-performance compute ('HPC') job schedulers
such as 'LSF', 'OpenLava', 'Slurm', 'SGE', and 'TORQUE' / 'PBS', e.g. 'y
<- future.apply::future_lapply(files, FUN = process)'.

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
