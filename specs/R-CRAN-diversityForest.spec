%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diversityForest
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Innovative Complex Split Procedures in Random Forests Through Candidate Split Sampling

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
Implements interaction forests [1], which are specific diversity forests
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
References: [1] Hornung, R. & Boulesteix, A.-L. (2022) Interaction
Forests: Identifying and exploiting interpretable quantitative and
qualitative interaction effects. Computational Statistics & Data Analysis
171:107460, <doi:10.1016/j.csda.2022.107460>. [2] Hornung, R. (2022)
Diversity forests: Using split sampling to enable innovative complex split
procedures in random forests. SN Computer Science 3(2):1,
<doi:10.1007/s42979-021-00920-1>.

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
