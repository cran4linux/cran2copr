%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lepidoptera
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Domain-Agnostic Causal Simulation Engine with Mixed Variable Types

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A domain-agnostic simulation engine for structural causal models with
heterogeneous variable types. Users define systems of continuous,
categorical, and ordinal features, declare a directed acyclic graph (DAG)
over them, attach typed generative mechanisms to each node, and simulate
synthetic populations. A pre-built mechanism library covers all nine
parent-type/child-type combinations. Vine copula mechanisms estimate full
joint dependence from observed data via pair-copula constructions (Bedford
and Cooke, 2002) <doi:10.1214/aos/1031689014>. Individual-level
counterfactual queries are supported through partial propagation, which
freezes unaffected random draws and resamples only the downstream
subgraph, enabling individual treatment effect (ITE) estimation alongside
population-level average treatment effects (ATE). Any pre-fitted
predictive model can serve as a generative mechanism through three wrapper
functions. Systems serialise to JSON for cross-language portability with
the companion Python package.

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
