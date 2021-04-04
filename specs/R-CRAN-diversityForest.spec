%global packname  diversityForest
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Complex Split Procedures in Random Forests Through Candidate Split Sampling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-sgeostat 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-MapGAM 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-sgeostat 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-MapGAM 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-survival 

%description
Implements interaction forests [1], which are specific diversity forests,
and the basic form of diversity forests that uses univariable, binary
splitting [2]. Interaction forests (IFs) are ensembles of decision trees
that model quantitative and qualitative interaction effects using
bivariable splitting. IFs come with the Effect Importance Measure (EIM),
which can be used to identify variable pairs that feature quantitative and
qualitative interaction effects with high predictive relevance. IFs and
EIM focus on well interpretable forms of interactions. The package also
offers plot functions for visualising the estimated forms of interaction
effects. Categorical, metric, and survival outcomes are supported. This is
a fork of the R package 'ranger' (main author: Marvin N. Wright) that
implements random forests using an efficient C++ implementation.
References: [1] Hornung, R. & Boulesteix, A.-L. (2021) Interaction
Forests: Identifying and exploiting interpretable quantitative and
qualitative interaction effects. Technical Report No. 237, Department of
Statistics, University of Munich [2] Hornung, R. (2020) Diversity Forests:
Using split sampling to allow for complex split procedures in random
forest. Technical Report No. 234, Department of Statistics, University of
Munich.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
