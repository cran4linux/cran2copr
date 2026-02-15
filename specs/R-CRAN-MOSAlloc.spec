%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MOSAlloc
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Constraint Multiobjective Sample Allocation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-ECOSolveR 
Requires:         R-CRAN-Matrix 

%description
Provides a framework for multipurpose optimal resource allocation in
survey sampling, extending the classical optimal allocation principles
introduced by Tschuprow (1923) and Neyman (1934) to multidomain and
multivariate allocation problems. The primary method mosalloc() allows for
the consideration of precision and cost constraints at the subpopulation
level while minimizing either a vector of sampling errors or survey costs
across a broad range of optimal sample allocation problems. The approach
supports both single- and multistage designs. For single-stage stratified
random sampling, the mosallocSTRS() function offers a user- friendly
interface. Sensitivity analysis is supported through the problem's dual
variables, which are naturally obtained via the internal use of the
Embedded Conic Solver from the 'ECOSolveR' package. See Willems (2025,
<doi:10.25353/ubtr-9200-484c-5c89>) for a detailed description of the
theory behind 'MOSAlloc'.

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
