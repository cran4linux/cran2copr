%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EGAnet
%global packver   2.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Graph Analysis – a Framework for Estimating the Number of Dimensions in Multivariate Data using Network Psychometrics

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph >= 1.3.0
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-fungible 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-GPArotation 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-semPlot 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph >= 1.3.0
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-fungible 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-GPArotation 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-network 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-semPlot 
Requires:         R-CRAN-sna 
Requires:         R-stats 

%description
Implements the Exploratory Graph Analysis (EGA) framework for
dimensionality and psychometric assessment. EGA estimates the number of
dimensions in psychological data using network estimation methods and
community detection algorithms. A bootstrap method is provided to assess
the stability of dimensions and items. Fit is evaluated using the Entropy
Fit family of indices. Unique Variable Analysis evaluates the extent to
which items are locally dependent (or redundant). Network loadings provide
similar information to factor loadings and can be used to compute network
scores. A bootstrap and permutation approach are available to assess
configural and metric invariance. Hierarchical structures can be detected
using Hierarchical EGA. Time series and intensive longitudinal data can be
analyzed using Dynamic EGA, supporting individual, group, and population
level assessments.

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
