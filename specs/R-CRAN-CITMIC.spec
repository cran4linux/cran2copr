%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CITMIC
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Cell Infiltration Based on Cell Crosstalk

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-stats 

%description
A systematic biology tool was developed to identify cell infiltration via
an Individualized Cell crosstalk network. 'CITMIC' first constructed a
weighted cell crosstalk network by integrating Cell-target interaction
information, biological process data from the Gene Ontology (GO) database,
and gene transcriptomic data in a specific sample, and then, it used a
network propagation algorithm on the network to identify cell infiltration
for the sample. Ultimately, cell infiltration in the patient dataset was
obtained by normalizing the centrality scores of the cells.

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
