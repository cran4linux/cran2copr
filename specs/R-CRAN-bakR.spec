%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bakR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze and Compare Nucleotide Recoding RNA Sequencing Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppParallel >= 5.0.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-rstantools >= 2.1.1
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-RcppParallel >= 5.0.1
Requires:         R-CRAN-rstantools >= 2.1.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rstantools

%description
Several implementations of a novel Bayesian hierarchical statistical model
of nucleotide recoding RNA-seq experiments (NR-seq; TimeLapse-seq,
SLAM-seq, TUC-seq, etc.) for analyzing and comparing NR-seq datasets (see
'Vock and Simon' (2023) <doi:10.1261/rna.079451.122>). NR-seq is a
powerful extension of RNA-seq that provides information about the kinetics
of RNA metabolism (e.g., RNA degradation rate constants), which is notably
lacking in standard RNA-seq data. The statistical model makes maximal use
of these high-throughput datasets by sharing information across
transcripts to significantly improve uncertainty quantification and
increase statistical power. 'bakR' includes a maximally efficient
implementation of this model for conservative initial investigations of
datasets. 'bakR' also provides more highly powered implementations using
the probabilistic programming language 'Stan' to sample from the full
posterior distribution. 'bakR' performs multiple-test adjusted statistical
inference with the output of these model implementations to help
biologists separate signal from background. Methods to automatically
visualize key results and detect batch effects are also provided.

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
