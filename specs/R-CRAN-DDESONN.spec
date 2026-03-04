%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DDESONN
%global packver   7.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          A Deep Dynamic Experimental Self-Organizing Neural Network Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-PRROC 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-ggplot2 

%description
Provides a fully native R deep learning framework for constructing,
training, evaluating, and inspecting Deep Dynamic Ensemble Self Organizing
Neural Networks at research scale. The core engine is an object oriented
R6 class-based implementation with explicit control over layer layout,
dimensional flow, forward propagation, back propagation, and transparent
optimizer state updates. The framework does not rely on external deep
learning back ends, enabling direct inspection of model state,
reproducible numerical behavior, and fine grained architectural control
without requiring compiled dependencies or graphics processing unit
specific run times. Users can define dimension agnostic single layer or
deep multi-layer networks without hard coded architecture limits, with per
layer configuration vectors for activation functions, derivatives, dropout
behavior, and initialization strategies automatically aligned to network
depth through controlled replication or truncation. Reproducible workflows
can be executed through high level helpers for fit, run, and predict
across binary classification, multi-class classification, and regression
modes. Training pipelines support optional self organization, adaptive
learning rate behavior, and structured ensemble orchestration in which
candidate models are evaluated under user specified performance metrics
and selectively promoted or pruned to refine a primary ensemble, enabling
controlled ensemble evolution over successive runs. Ensemble evaluation
includes fused prediction strategies in which member outputs may be
combined through weighted averaging, arithmetic averaging, or voting
mechanisms to generate consolidated metrics for research level comparison
and reproducible per-seed assessment. The framework supports multiple
optimization approaches, including stochastic gradient descent, adaptive
moment estimation, and look ahead methods, alongside configurable
regularization controls such as L1, L2, and mixed penalties with separate
weight and bias update logic. Evaluation features provide threshold
tuning, relevance scoring, receiver operating characteristic and precision
recall curve generation, area under curve computation, regression error
diagnostics, and report ready metric outputs. The package also includes
artifact path management, debug state utilities, structured run level
metadata persistence capturing seeds, configuration states, thresholds,
metrics, ensemble transitions, fused evaluation artifacts, and model
identifiers, as well as reproducible scripts and vignettes documenting end
to end experiments. Kingma and Ba (2015) <doi:10.48550/arXiv.1412.6980>
"Adam: A Method for Stochastic Optimization". Hinton et al. (2012)
<https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf>
"Neural Networks for Machine Learning (RMSprop lecture notes)". Duchi et
al. (2011) <https://jmlr.org/papers/v12/duchi11a.html> "Adaptive
Subgradient Methods for Online Learning and Stochastic Optimization".
Zeiler (2012) <doi:10.48550/arXiv.1212.5701> "ADADELTA: An Adaptive
Learning Rate Method". Zhang et al. (2019) <doi:10.48550/arXiv.1907.08610>
"Lookahead Optimizer: k steps forward, 1 step back". You et al. (2019)
<doi:10.48550/arXiv.1904.00962> "Large Batch Optimization for Deep
Learning: Training BERT in 76 minutes (LAMB)". McMahan et al. (2013)
<https://research.google.com/pubs/archive/41159.pdf> "Ad Click Prediction:
a View from the Trenches (FTRL-Proximal)". Klambauer et al. (2017)
<https://proceedings.neurips.cc/paper/6698-self-normalizing-neural-networks.pdf>
"Self-Normalizing Neural Networks (SELU)". Maas et al. (2013)
<https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf>
"Rectifier Nonlinearities Improve Neural Network Acoustic Models (Leaky
ReLU / rectifiers)".

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
