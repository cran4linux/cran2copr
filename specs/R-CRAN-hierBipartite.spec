%global packname  hierBipartite
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bipartite Graph-Based Hierarchical Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-irlba 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-irlba 

%description
Bipartite graph-based hierarchical clustering, developed for
pharmacogenomic datasets and datasets sharing the same data structure. The
goal is to construct a hierarchical clustering of groups of samples based
on association patterns between two sets of variables. In the context of
pharmacogenomic datasets, the samples are cell lines, and the two sets of
variables are typically expression levels and drug sensitivity values. For
this method, sparse canonical correlation analysis from Lee, W., Lee, D.,
Lee, Y. and Pawitan, Y. (2011) <doi:10.2202/1544-6115.1638> is first
applied to extract association patterns for each group of samples. Then, a
nuclear norm-based dissimilarity measure is used to construct a
dissimilarity matrix between groups based on the extracted associations.
Finally, hierarchical clustering is applied.

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
