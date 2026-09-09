%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  octawave
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Octahedral Quantum Wave Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-plotly 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-plotly 

%description
Provides mathematical tools for simulating and visualizing
three-dimensional octahedral quantum wave interferences and spatial
resonance fields. Includes functions for MRI slice generation of fullerene
structures and wave models. Computational modeling and three-dimensional
visualization of fullerene and octahedral topologies are implemented
within the R statistical environment, with interactive plotting powered by
'plotly'. Theoretical foundations are based on the topological frameworks
of Cataldo et al. (2015) <doi:10.1002/wcms.1207>, Dresselhaus et al.
(1996, ISBN:9780122218200), and Coxeter (1973, ISBN:9780486614809); the
geometric principles of equations of the octahedron type are outlined in
Bobenko and Suris (2012) <doi:10.1093/imrn/rnr083>. Additional structural
and biological symmetry contexts are derived from Bragg (1914)
<doi:10.1098/rspa.1914.0015> and Caspar and Klug (1962)
<doi:10.1101/sqb.1962.027.001.005>.

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
