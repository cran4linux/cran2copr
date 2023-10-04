%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  graphseg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Segmentation of Graph-Based Signals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-flsa 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-flsa 

%description
Perform segmentation of graph-based signals. Assume a noisy observation of
a signal two values correspond to vertices on a graph. Assume the true
value of the signal is piece-wise constant (where each 'piece' is a
connected subgraph). The main function, agraph(), computes the
segmentation of the signal. The package also includes a wrapper around the
competing method flsa() (from package 'flsa'). More information about this
method in Goepp and van de Kassteele (2022) "Graph-Based Spatial
Segmentation of Health-Related Areal Data"
<doi:10.48550/arXiv.2206.06752>.

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
