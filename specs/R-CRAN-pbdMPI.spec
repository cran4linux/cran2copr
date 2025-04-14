%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pbdMPI
%global packver   0.5-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to MPI for HPC Clusters (Programming with Big Data Project)

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
Requires:         openmpi%{_isa}
BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-float 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-float 
Requires:         R-parallel 

%description
A simplified, efficient, interface to MPI for HPC clusters. It is a
derivation and rethinking of the Rmpi package. pbdMPI embraces the
prevalent parallel programming style on HPC clusters. Beyond the
interface, a collection of functions for global work with distributed data
and resource-independent RNG reproducibility is included. It is based on
S4 classes and methods.

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
