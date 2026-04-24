%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BrainNetTest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hypothesis Testing for Populations of Brain Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 

%description
Non-parametric hypothesis testing for populations of brain networks
represented as graphs, following the L1-distance ANOVA framework of
Fraiman and Fraiman (2018) <doi:10.1038/s41598-018-21688-0>. The package
builds on this nonparametric graph-comparison framework, extending it with
procedures for edge-level inference and identification of the specific
connections driving group differences. In particular, it provides
utilities to compute central (mean) graphs, pairwise Manhattan distances
between adjacency matrices, the group test statistic T, and a fast
permutation procedure to identify the critical edges that drive
between-group differences. Helper functions to generate synthetic
community-structured graphs and to visualise brain networks with
communities are also included.

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
