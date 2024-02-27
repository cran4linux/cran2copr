%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesCVI
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Cluster Validity Index

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-UniversalCVI 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-UniversalCVI 

%description
Algorithms for computing and generating plots with and without error bars
for Bayesian cluster validity index (BCVI) (N. Wiroonsri, O. Preedasawakul
(2024) <arXiv:2402.02162>) based on several underlying cluster validity
indexes (CVIs) including Calinski-Harabasz, Chou-Su-Lai, Davies-Bouldin,
Dunn, Pakhira-Bandyopadhyay-Maulik, Point biserial correlation, the score
function, Starczewski, and Wiroonsri indices for hard clustering, and
Correlation Cluster Validity, the generalized C, HF, KWON, KWON2, Modified
Pakhira-Bandyopadhyay-Maulik, Pakhira-Bandyopadhyay-Maulik, Tang,
Wiroonsri-Preedasawakul, Wu-Li, and Xie-Beni indices for soft clustering.
The package is compatible with K-means, fuzzy C means, EM clustering, and
hierarchical clustering (single, average, and complete linkage). Though
BCVI is compatible with any underlying existing CVIs, we recommend users
to use either WI or WP as the underlying CVI.

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
