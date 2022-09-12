%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  archeofrag
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Refitting and Spatial Analysis in Archaeology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-utils 

%description
Methods to analyse fragmented objects in archaeology using refitting
relationships between fragments scattered in archaeological spatial units
(e.g. stratigraphic layers). Graphs and graph theory are used to model
archaeological observations. The package is mainly based on the 'igraph'
package for graph analysis. Functions can: 1) create, manipulate, and
simulate fragmentation graphs, 2) measure the cohesion and admixture of
archaeological spatial units, and 3) characterise the topology of a
specific set of refitting relationships. An empirical dataset is also
provided as an example. Documentation about 'archeofrag' is provided by
the vignette included in this package and by the accompanying scientific
papers: Plutniak (2021, Journal of Archaeological Science,
<doi:10.1016/j.jas.2021.105501>) and Plutniak (2022, Journal of Open
Source Software, <doi:10.21105/joss.04335>).

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
