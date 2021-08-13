%global __brp_check_rpaths %{nil}
%global packname  rgexf
%global packver   0.16.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16.2
Release:          1%{?dist}%{?buildtag}
Summary:          Build, Import and Export GEXF Graph Files

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-servr 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-igraph 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-servr 

%description
Create, read and write 'GEXF' (Graph Exchange 'XML' Format) graph files
(used in 'Gephi' and others). Using the 'XML' package, it allows the user
to easily build/read graph files including attributes, 'GEXF' visual
attributes (such as color, size, and position), network dynamics (for both
edges and nodes) and edge weighting. Users can build/handle graphs
element-by-element or massively through data-frames, visualize the graph
on a web browser through 'gexf-js' (a 'javascript' library) and interact
with the 'igraph' package.

%prep
%setup -q -c -n %{packname}
sed -i '/system.file/d' %{packname}/man/plot.gexf.Rd
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
