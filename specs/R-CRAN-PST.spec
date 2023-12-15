%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PST
%global packver   0.94.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.94.1
Release:          1%{?dist}%{?buildtag}
Summary:          Probabilistic Suffix Trees and Variable Length Markov Chains

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
Requires:         R-CRAN-TraMineR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-methods 
Requires:         R-stats4 

%description
Provides a framework for analysing state sequences with probabilistic
suffix trees (PST), the construction that stores variable length Markov
chains (VLMC). Besides functions for learning and optimizing VLMC models,
the PST library includes many additional tools to analyse sequence data
with these models: visualization tools, functions for sequence prediction
and artificial sequences generation, as well as for context and pattern
mining. The package is specifically adapted to the field of social
sciences by allowing to learn VLMC models from sets of individual
sequences possibly containing missing values, and by accounting for case
weights. The library also allows to compute probabilistic divergence
between two models, and to fit segmented VLMC, where sub-models fitted to
distinct strata of the learning sample are stored in a single PST. This
software results from research work executed within the framework of the
Swiss National Centre of Competence in Research LIVES, which is financed
by the Swiss National Science Foundation. The authors are grateful to the
Swiss National Science Foundation for its financial support.

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
