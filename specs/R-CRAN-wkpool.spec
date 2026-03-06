%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wkpool
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Vertex Pool Topology for Well-Known Geometry

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-wk >= 0.9.4
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-wk >= 0.9.4
Requires:         R-CRAN-vctrs 

%description
Establishes and maintains vertex pool topology for geometry handled by
'wk'. Segments are the atomic unit, vertices are shared via integer
references into a pool. Topology is made discoverable via coincident
vertex detection while not requiring modification of the input data.
Topological data models follow principles described in Worboys and Duckham
(2004, ISBN:978-0415283755). The edge-based topology geometry decomposed
into vertices and directed edge pairs is a simplification of the quad-edge
case in Guibas & Stolfi (1985) <doi:10.1145/282918.282923>.

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
