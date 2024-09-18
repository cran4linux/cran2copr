%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  miic
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Learning Causal or Non-Causal Graphical Models Using Information Theory

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
Multivariate Information-based Inductive Causation, better known by its
acronym MIIC, is a causal discovery method, based on information theory
principles, which learns a large class of causal or non-causal graphical
models from purely observational data, while including the effects of
unobserved latent variables. Starting from a complete graph, the method
iteratively removes dispensable edges, by uncovering significant
information contributions from indirect paths, and assesses edge-specific
confidences from randomization of available data. The remaining edges are
then oriented based on the signature of causality in observational data.
The recent more interpretable MIIC extension (iMIIC) further distinguishes
genuine causes from putative and latent causal effects, while scaling to
very large datasets (hundreds of thousands of samples). Since the version
2.0, MIIC also includes a temporal mode (tMIIC) to learn temporal causal
graphs from stationary time series data. MIIC has been applied to a wide
range of biological and biomedical data, such as single cell gene
expression data, genomic alterations in tumors, live-cell time-lapse
imaging data (CausalXtract), as well as medical records of patients. MIIC
brings unique insights based on causal interpretation and could be used in
a broad range of other data science domains (technology, climatology,
economy, ...). For more information, you can refer to: Simon et al., eLife
2024, <doi:10.1101/2024.02.06.579177>, Ribeiro-Dantas et al., iScience
2024, <doi:10.1016/j.isci.2024.109736>, Cabeli et al., NeurIPS 2021,
<https://why21.causalai.net/papers/WHY21_24.pdf>, Cabeli et al., Comput.
Biol. 2020, <doi:10.1371/journal.pcbi.1007866>, Li et al., NeurIPS 2019,
<https://papers.nips.cc/paper/9573-constraint-based-causal-structure-learning-with-consistent-separating-sets>,
Verny et al., PLoS Comput. Biol. 2017, <doi:10.1371/journal.pcbi.1005662>,
Affeldt et al., UAI 2015,
<https://auai.org/uai2015/proceedings/papers/293.pdf>. Changes from the
previous 1.5.3 release on CRAN are available at
<https://github.com/miicTeam/miic_R_package/blob/master/NEWS.md>.

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
