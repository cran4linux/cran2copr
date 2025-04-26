%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metasnf
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Meta Clustering with Similarity Network Fusion

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SNFtool 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SNFtool 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Framework to facilitate patient subtyping with similarity network fusion
and meta clustering. The similarity network fusion (SNF) algorithm was
introduced by Wang et al. (2014) in <doi:10.1038/nmeth.2810>. SNF is a
data integration approach that can transform high-dimensional and diverse
data types into a single similarity network suitable for clustering with
minimal loss of information from each initial data source. The meta
clustering approach was introduced by Caruana et al. (2006) in
<doi:10.1109/ICDM.2006.103>. Meta clustering involves generating a wide
range of cluster solutions by adjusting clustering hyperparameters, then
clustering the solutions themselves into a manageable number of
qualitatively similar solutions, and finally characterizing representative
solutions to find ones that are best for the user's specific context. This
package provides a framework to easily transform multi-modal data into a
wide range of similarity network fusion-derived cluster solutions as well
as to visualize, characterize, and validate those solutions. Core package
functionality includes easy customization of distance metrics, clustering
algorithms, and SNF hyperparameters to generate diverse clustering
solutions; calculation and plotting of associations between features,
between patients, and between cluster solutions; and standard cluster
validation approaches including resampled measures of cluster stability,
standard metrics of cluster quality, and label propagation to evaluate
generalizability in unseen data. Associated vignettes guide the user
through using the package to identify patient subtypes while adhering to
best practices for unsupervised learning.

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
