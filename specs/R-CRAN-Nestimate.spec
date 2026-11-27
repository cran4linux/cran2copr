%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Nestimate
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic, Probabilistic, and Higher-Order Network Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-psychnets >= 0.5.2
BuildRequires:    R-CRAN-idiographic >= 0.3.4
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-brglm2 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-psychnets >= 0.5.2
Requires:         R-CRAN-idiographic >= 0.3.4
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-brglm2 
Requires:         R-CRAN-nnet 

%description
Estimates, compares and tests networks from sequence, event-log, panel and
cross-sectional data through one interface, build_network(). Sequence data
give transition, frequency, co-occurrence, attention-weighted, n-gram, gap
and reply networks, following transition network analysis Saqr et al.
(2025) <doi:10.1145/3706468.3706513>, and reply networks weighted by
response latency Templeton et al. (2022) <doi:10.1073/pnas.2116915119>.
Psychological networks are estimated by correlation, partial correlation,
graphical lasso, Ising and mixed graphical models Saqr, Beck, and
Lopez-Pernas (2024) <doi:10.1007/978-3-031-54464-4_19>, together with
multilevel vector autoregression Epskamp et al. (2018)
<doi:10.1080/00273171.2018.1454823> and the network comparison test van
Borkulo et al. (2022) <doi:10.1037/met0000476>. Higher-order methods cover
higher-order networks, hyper-path anomalies, multi-order generative
models, hypergraphs and simplicial complexes. Inference includes
bootstrap, permutation and Bayesian comparison, split-half reliability and
centrality stability. Further tools fit mixtures of Markov chains and
cluster sequences, test Markov order, and compute transition entropy,
passage times, stability landscapes, sequence patterns and indices, and
association tests for counts nested in actors.

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
