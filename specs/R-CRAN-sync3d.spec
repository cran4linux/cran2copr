%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sync3d
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Synchronized 3D Vector and Marker Animations in 'Plotly'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-plotly 

%description
Provides a domain-agnostic visualization utility designed to bypass
structural rendering limitations within multi-trace three-dimensional
animations in 'Plotly' by implementing a decoupled rendering pipeline.
Computational processing of time-dependent physical states (markers and
nodes) is managed within the R environment, while a custom
hardware-accelerated 'WebGL' injection handles the synchronous rendering
of complex topological frameworks (lines and edges) directly within the
'UI' browser interface via 'htmlwidgets'. This dual-layer architecture
ensures smooth execution of synchronized multi-component 3D animations
without framework degradation or controller loss.

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
