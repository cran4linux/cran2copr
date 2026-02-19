%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetworkComparisonTest
%global packver   2.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Comparison of Two Networks Based on Several Invariance Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-networktools 
BuildRequires:    R-CRAN-IsingFit 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-networktools 
Requires:         R-CRAN-IsingFit 

%description
This permutation based hypothesis test, suited for several types of data
supported by the estimateNetwork function of the bootnet package (Epskamp
& Fried, 2018), assesses the difference between two networks based on
several invariance measures (network structure invariance, global strength
invariance, edge invariance, several centrality measures, etc.). Network
structures are estimated with l1-regularization. The Network Comparison
Test is suited for comparison of independent (e.g., two different groups)
and dependent samples (e.g., one group that is measured twice). See van
Borkulo et al. (2021), available from <doi:10.1037/met0000476>.

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
