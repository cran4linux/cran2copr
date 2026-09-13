%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AutoGenAI
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Optimization of Prompts, Models and Generation Strategies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-jsonlite 

%description
Provides provider-agnostic tools for jointly comparing and optimizing
prompts, language-model providers, and generation strategies for
generative artificial intelligence workflows. Candidate configurations can
be evaluated using user-supplied scoring functions, cost and latency
measurements, robustness perturbations, Pareto-front screening, budget and
latency constraints, prompt evolution, adaptive routing, self-consistency,
and text-output ensembles. The core workflow is designed to run offline
with deterministic mock providers, while external model application
programming interfaces can be connected through user-defined provider
functions. Evolutionary search concepts are described by Goldberg (1989,
ISBN:0201157675), and multi-objective optimization concepts are related to
Deb, Pratap, Agarwal and Meyarivan (2002) <doi:10.1109/4235.996017>.

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
