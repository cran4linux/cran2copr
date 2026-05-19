%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cclustr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Consensus Clustering Methods for Multiple Imputed Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-fpc 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-clustMixType 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-mclust 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-fpc 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-clustMixType 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-mclust 

%description
Provides tools for performing consensus clustering on multiple imputed
datasets. The package supports a range of clustering algorithms across
imputations, including hierarchical methods (e.g., Ward, single, complete,
average) and partition-based approaches such as k-means, k-medoids (PAM),
fuzzy clustering, model-based clustering ('mclust'), and methods for mixed
or categorical data (k-modes and k-prototypes). A co-assignment matrix is
constructed to quantify agreement between partitions, and consensus
solutions are derived via hierarchical clustering applied to the resulting
dissimilarity matrix. Additional functions are provided for validation and
visualization of clustering results, facilitating robust analysis in the
presence of missing data. Consensus clustering framework is based on Monti
et al. (2003) <doi:10.1023/A:1023949509487>, rank aggregation methods
follow Pihur et al. (2007) <doi:10.1093/bioinformatics/btm158>, and the
PAC (Proportion of Ambiguous Clustering) metric is based on Senbabaoglu et
al. (2014) <doi:10.1038/srep06207>.

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
