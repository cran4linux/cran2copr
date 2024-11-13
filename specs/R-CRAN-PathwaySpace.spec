%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PathwaySpace
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Projection of Network Signals along Geodesic Paths

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RGraphSpace 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-methods 
Requires:         R-CRAN-RGraphSpace 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 

%description
For a given graph containing vertices, edges, and a signal associated with
the vertices, the 'PathwaySpace' package performs a convolution operation,
which involves a weighted combination of neighboring vertices and their
associated signals. The package then uses a decay function to project
these signals, creating geodesic paths on a 2D-image space. 'PathwaySpace'
could have various applications, such as visualizing and analyzing network
data in a graphical format that highlights the relationships and signal
strengths between vertices. It can be particularly useful for
understanding the influence of signals through complex networks. By
combining graph theory, signal processing, and visualization, the
'PathwaySpace' package provides a novel way of representing and analyzing
graph data.

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
