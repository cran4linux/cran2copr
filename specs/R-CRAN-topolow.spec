%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  topolow
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Force-Directed Euclidean Embedding of Dissimilarity Data

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-parallel >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-filelock 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-rlang 
Requires:         R-parallel >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-future 
Requires:         R-CRAN-lifecycle 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-filelock 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-rlang 

%description
A robust implementation of Topolow algorithm. It embeds objects into a
low-dimensional Euclidean space from a matrix of pairwise dissimilarities,
even when the data do not satisfy metric or Euclidean axioms. The package
is particularly well-suited for sparse, incomplete, and censored
(thresholded) datasets such as antigenic relationships. The core is a
physics-inspired, gradient-free optimization framework that models objects
as particles in a physical system, where observed dissimilarities define
spring rest lengths and unobserved pairs exert repulsive forces. The
package also provides functions specific to antigenic mapping to transform
cross-reactivity and binding affinity measurements into accurate spatial
representations in a phenotype space. Key features include: * Robust
Embedding from Sparse Data: Effectively creates complete and consistent
maps (in optimal dimensions) even with high proportions of missing data
(e.g., >95%%). * Physics-Inspired Optimization: Models objects (e.g.,
antigens, landmarks) as particles connected by springs (for measured
dissimilarities) and subject to repulsive forces (for missing
dissimilarities), and simulates the physical system using laws of
mechanics, reducing the need for complex gradient computations. *
Automatic Dimensionality Detection: Employs a likelihood-based approach to
determine the optimal number of dimensions for the embedding/map, avoiding
distortions common in methods with fixed low dimensions. * Noise and Bias
Reduction: Naturally mitigates experimental noise and bias through its
network-based, error-dampening mechanism. * Antigenic Velocity Calculation
(for antigenic data): Introduces and quantifies "antigenic velocity," a
vector that describes the rate and direction of antigenic drift for each
pathogen isolate. This can help identify cluster transitions and potential
lineage replacements. * Broad Applicability: Analyzes data from various
objects that their dissimilarity may be of interest, ranging from complex
biological measurements such as continuous and relational phenotypes,
antibody-antigen interactions, and protein folding to abstract concepts,
such as customer perception of different brands. Methods are described in
the context of bioinformatics applications in Arhami and Rohani (2025a)
<doi:10.1093/bioinformatics/btaf372>, and mathematical proofs and
Euclidean embedding details are in Arhami and Rohani (2025b)
<doi:10.48550/arXiv.2508.01733>.

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
