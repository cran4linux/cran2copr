%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pbdMPI
%global packver   0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}%{?buildtag}
Summary:          Programming with Big Data -- Interface to MPI

License:          Mozilla Public License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    openmpi-devel
Requires:         openmpi%{_isa}
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlecuyer 
BuildRequires:    R-CRAN-float 
Requires:         R-methods 
Requires:         R-CRAN-rlecuyer 
Requires:         R-CRAN-float 

%description
An efficient interface to MPI by utilizing S4 classes and methods with a
focus on Single Program/Multiple Data ('SPMD') parallel programming style,
which is intended for batch parallel execution.

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
