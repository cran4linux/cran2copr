%global packname  DynComm
%global packver   2020.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2020.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Network Communities Detection and Generation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 

%description
Used for evolving network analysis regarding community detection.
Implements several algorithms that calculate communities for graphs whose
nodes and edges change over time. Edges, which can have new nodes, can be
added or deleted. Changes in the communities are calculated without
recalculating communities for the entire graph. REFERENCE: M. Cordeiro et
al. (2016) <DOI:10.1007/s13278-016-0325-1> G. Rossetti et al. (2017)
<DOI:10.1007/s10994-016-5582-8> G. Rossetti (2017)
<DOI:10.1093/comnet/cnx016> R. Sarmento (2019) <arXiv:1904.12593>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
