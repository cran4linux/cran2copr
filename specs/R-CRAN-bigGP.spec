%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bigGP
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Distributed Gaussian Process Calculations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
Requires:         openmpi%{_isa}
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rmpi >= 0.6.2
BuildRequires:    R-methods 
Requires:         R-CRAN-Rmpi >= 0.6.2
Requires:         R-methods 

%description
Distributes Gaussian process calculations across nodes in a distributed
memory setting, using Rmpi. The bigGP class provides high-level methods
for maximum likelihood with normal data, prediction, calculation of
uncertainty (i.e., posterior covariance calculations), and simulation of
realizations. In addition, bigGP provides an API for basic matrix
calculations with distributed covariance matrices, including Cholesky
decomposition, back/forwardsolve, crossproduct, and matrix multiplication.

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
%{_openmpi_load}
export MPI_LIB_PATH=$MPI_LIB
export MPI_TYPE=OPENMPI
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
%{_openmpi_unload}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
