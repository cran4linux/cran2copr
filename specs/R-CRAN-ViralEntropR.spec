%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ViralEntropR
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Computational Pipeline for Entropy-Informed Detection of Emerging Viral Variants

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-HDcpDetect 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-grDevices 
Requires:         R-CRAN-HDcpDetect 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Implements an entropy-informed pipeline for detecting emerging variants in
viral amino acid sequence data, extending prior clustering-based
approaches including hemagglutinin clustering methods (Li et al., 2015)
<doi:10.1142/9789814667944_0018>. Provides a fully vectorized FASTA
preprocessing toolkit covering header parsing, two-pass date and country
extraction, ambiguous-residue filtering, and integer encoding under a
25-symbol amino acid alphabet. Computes per-site Shannon entropy across
user-defined cumulative, sliding, or disjoint temporal partitions and
clusters per-site entropy values using Gaussian mixture models via
'mclust' (Scrucca et al., 2016) <doi:10.32614/RJ-2016-021>. Quantifies
temporal distributional shifts between partitions using the Hellinger
distance (van der Vaart, 1998) <doi:10.1017/CBO9780511802256>, and detects
temporal change points non-parametrically using energy statistics
(Matteson and James, 2014) <doi:10.1080/01621459.2013.849605> via 'ecp' or
wild binary segmentation (Fryzlewicz, 2014) <doi:10.1214/14-AOS1245> via
'HDcpDetect'. Per-site amino-acid frequency tables and entropy trajectory
plots characterize sequence composition and evolutionary dynamics across
time. A configurable multi-variant simulation engine generates synthetic
sequence time series with known ground truth for benchmarking detection
pipelines. A curated dataset of SARS-CoV-2 Variants of Concern and
Variants of Interest with associated lineage and surveillance metadata is
included, along with a bundled National Center for Biotechnology
Information (NCBI) Spike protein sample and vignettes demonstrating the
full workflow.

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
