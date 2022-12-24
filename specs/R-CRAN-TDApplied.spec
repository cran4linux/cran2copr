%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TDApplied
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning and Inference for Topological Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-rdist 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-rdist 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-iterators 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Topological data analysis is a powerful tool for finding non-linear global
structure in whole datasets. 'TDApplied' aims to bridge topological data
analysis with data, statistical and machine learning practitioners so that
more analyses may benefit from the power of topological data analysis. The
main tool of topological data analysis is persistent homology, which
computes a shape descriptor of a dataset, called a persistence diagram.
There are five goals of this package: (1) deliver a fast implementation of
persistent homology via a python interface, (2) convert persistence
diagrams computed using the two main R packages for topological data
analysis into a data frame, (3) implement fast versions of both distance
and kernel calculations for pairs of persistence diagrams, (4) contribute
tools for the interpretation of persistence diagrams, and (5) provide
parallelized methods for machine learning and inference for persistence
diagrams.

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
