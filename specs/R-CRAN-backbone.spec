%global __brp_check_rpaths %{nil}
%global packname  backbone
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Extracts the Backbone from Graphs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-PoissonBinomial 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-network 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-PoissonBinomial 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 

%description
An implementation of methods for extracting an unweighted unipartite graph
(i.e. a backbone) from an unweighted unipartite graph (Hamann et al., 2016
<doi:10.1007/s13278-016-0332-2>), a weighted unipartite graph (Serrano et
al., 2009 <doi:10.1073/pnas.0808904106>), the projection of an unweighted
bipartite graph (Neal et al., <doi:10.1038/s41598-021-03238-3>, or the
projection of a weighted bipartite graph (Neal, 2017
<doi:10.1177/0308518X16631339>). It also provides utility functions to
generate random binary matrices with (a) given density, (b) given row and
column marginals, and (c) given row and column marginal distributions.

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
