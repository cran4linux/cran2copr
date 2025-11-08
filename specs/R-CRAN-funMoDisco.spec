%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funMoDisco
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Motif Discovery in Functional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggtext 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-class 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 

%description
Efficiently implementing two complementary methodologies for discovering
motifs in functional data: ProbKMA and FunBIalign. Cremona and Chiaromonte
(2023) "Probabilistic K-means with Local Alignment for Clustering and
Motif Discovery in Functional Data" <doi:10.1080/10618600.2022.2156522> is
a probabilistic K-means algorithm that leverages local alignment and fuzzy
clustering to identify recurring patterns (candidate functional motifs)
across and within curves, allowing different portions of the same curve to
belong to different clusters. It includes a family of distances and a
normalization to discover various motif types and learns motif lengths in
a data-driven manner. It can also be used for local clustering of
misaligned data. Di Iorio, Cremona, and Chiaromonte (2023) "funBIalign: A
Hierarchical Algorithm for Functional Motif Discovery Based on Mean
Squared Residue Scores" <doi:10.48550/arXiv.2306.04254> applies
hierarchical agglomerative clustering with a functional generalization of
the Mean Squared Residue Score to identify motifs of a specified length in
curves. This deterministic method includes a small set of user-tunable
parameters. Both algorithms are suitable for single curves or sets of
curves. The package also includes a flexible function to simulate
functional data with embedded motifs, allowing users to generate benchmark
datasets for validating and comparing motif discovery methods.

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
