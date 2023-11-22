%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustermq
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluate Function Calls on HPC Schedulers (LSF, SGE, SLURM, PBS/Torque)

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zeromq-devel
BuildRequires:    R-devel >= 3.6.2
Requires:         R-core >= 3.6.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-narray 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-narray 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
Evaluate arbitrary function calls using workers on HPC schedulers in
single line of code. All processing is done on the network without
accessing the file system. Remote schedulers are supported via SSH.

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
