%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Nestimate
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Network Estimation, Bootstrap, and Higher-Order Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-scales 

%description
Estimate, compare, and analyze dynamic and psychological networks using a
unified interface. Provides transition network analysis estimation
(transition, frequency, co-occurrence, attention-weighted) Saqr et al.
(2025) <doi:10.1145/3706468.3706513>, psychological network methods
(correlation, partial correlation, 'graphical lasso', 'Ising') Saqr, Beck,
and Lopez-Pernas (2024) <doi:10.1007/978-3-031-54464-4_19>, and
higher-order network methods including higher-order networks, higher-order
network embedding, hyper-path anomaly, and multi-order generative model.
Supports bootstrap inference, permutation testing, split-half reliability,
centrality stability analysis, mixed Markov models, multi-cluster
multi-layer networks and clustering.

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
