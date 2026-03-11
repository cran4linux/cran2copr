%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baycn
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Inference for Causal Networks

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-expm 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-expm 

%description
An approximate Bayesian method for inferring Directed Acyclic Graphs
(DAGs) for continuous, discrete, and mixed data. The algorithm can use the
graph inferred by another more efficient graph inference method as input;
the input graph may contain false edges or undirected edges but can help
reduce the search space to a more manageable size. A
Metropolis-Hastings-like sampling algorithm is then used to infer the
posterior probabilities of edge direction and edge absence. References:
Martin, Patchigolla and Fu (2026) <doi:10.48550/arXiv.1909.10678>.

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
