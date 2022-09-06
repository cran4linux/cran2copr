%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  meteoEVT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Visualization of Energetic and Vortical Atmospheric Quantities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ncdf4 

%description
Energy-Vorticity theory (EVT) is the fundamental theory to describe
processes in the atmosphere by combining conserved quantities from
hydrodynamics and thermodynamics. The package 'meteoEVT' provides
functions to calculate many energetic and vortical quantities, like
potential vorticity, Bernoulli function and dynamic state index (DSI)
[e.g. Weber and Nevir, 2008, <doi:10.1111/j.1600-0870.2007.00272.x>], for
given gridded data, like ERA5 reanalyses. These quantities can be studied
directly or can be used for many applications in meteorology, e.g., the
objective identification of atmospheric fronts. For this purpose, separate
function are provided that allow the detection of fronts based on the
thermic front parameter [Hewson, 1998, <doi:10.1017/S1350482798000553>],
the F diagnostic [Parfitt et al., 2017, <doi:10.1002/2017GL073662>] and
the DSI [Mack et al., 2022, <arXiv:2208.11438>].

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
