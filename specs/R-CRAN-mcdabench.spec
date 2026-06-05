%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcdabench
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmarking for Multi-Criteria Decision Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-monochromeR 
BuildRequires:    R-CRAN-networkD3 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-monochromeR 
Requires:         R-CRAN-networkD3 

%description
Performs and benchmarks various Multi-Criteria Decision Analysis (MCDA)
methods. MCDA is a decision-making framework used to evaluate and rank
alternatives based on multiple conflicting criteria using normalization,
weighting, and aggregation techniques. The package implements a wide range
of MCDA methods including ARAS (Additive Ratio Assessment), AROMAN
(Alternative Ranking Order Method Accounting for two-step Normalization),
COCOSO (Combined Compromise Solution), CODAS (Combinative Distance-based
Assessment), COPRAS (Complex Proportional Assessment), EDAS (Evaluation
based on Distance from Average Solution), ELECTRE (Elimination and Choice
Expressing Reality) family (I-IV), FUCA (Faire Un Choix Adequat), GRA
(Grey Relational Analysis), MABAC (Multi-Attributive Border Approximation
Area Comparison), MAIRCA (Multi-Attributive Ideal-Real Comparative
Analysis), MARCOS (Measurement of Alternatives and Ranking according to
Compromise Solution), MAUT (Multi-Attribute Utility Theory), MAVT
(Multi-Attribute Value Theory), MEGAN (Multi-criteria Evaluation with
Gradual-weighting and Aggregation of Normalized distance matrices), MOORA
(Multi-Objective Optimization on the basis of Ratio Analysis), OCRA
(Operational Competitiveness Rating Analysis), ORESTE (Organisation,
Rangement Et Synthese De Donnees Relationnelles), PROMETHEE (Preference
Ranking Organization Method for Enrichment Evaluations I-VI), RAM (Root
Assessment Method), ROV (Range of Value), SMART (Simple Multi-Attribute
Rating Technique), TOPSIS (Technique for Order Preference by Similarity to
Ideal Solution), VIKOR (VlseKriterijumska Optimizacija I Kompromisno
Resenje), WASPAS (Weighted Aggregated Sum Product Assessment), WPM
(Weighted Product Model), and WSM (Weighted Sum Model). The package
computes comparative evaluation measures including Spearman rank
correlation (Spearman, 1904) <doi:10.2307/1412107>, Salabun-Urbaniak's
weight similarity index (Salabun and Urbaniak,
2020)<doi:10.1007/978-3-030-50417-5_47>, Wilcoxon signed-rank test
(Wilcoxon, 1945)<doi:10.2307/3001968>, and permutation- and bootstrap-
based entropy difference tests for pairwise method comparisons using
Jensen-Shannon divergence (Lin, 1991)<doi:10.1109/18.61115>. It also
provides sensitivity and stability analysis of MCDA results. Weight
sensitivity analysis is implemented through deterministic and stochastic
perturbation of criterion weights, and is also integrated as a built-in
step within the MEGAN method framework (Cebeci,
2026)<doi:10.7717/peerj-cs.3819>.

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
