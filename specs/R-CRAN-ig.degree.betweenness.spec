%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ig.degree.betweenness
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          "Smith-Pittman Community Detection Algorithm for 'igraph' Objects (2024)"

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-igraphdata 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-BBmisc 
BuildRequires:    R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-igraphdata 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-BBmisc 
Requires:         R-CRAN-qgraph 

%description
Implements the "Smith-Pittman" community detection algorithm for network
analysis using 'igraph' objects. This algorithm combines node degree and
betweenness centrality measures to identify communities within networks,
with a gradient evident in social partitioning. The package provides
functions for community detection, visualization, and analysis of the
resulting community structure. Methods are based on results from Smith,
Pittman and Xu (2024) <doi:10.48550/arXiv.2411.01394>.

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
