%global __brp_check_rpaths %{nil}
%global packname  wTO
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computing Weighted Topological Overlaps (wTO) & Consensus wTO Network

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-HiClimR 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 
Requires:         R-CRAN-som 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-HiClimR 
Requires:         R-methods 

%description
Computes the Weighted Topological Overlap with positive and negative signs
(wTO) networks given a data frame containing the mRNA count/ expression/
abundance per sample, and a vector containing the interested nodes of
interaction (a subset of the elements of the full data frame). It also
computes the cut-off threshold or p-value based on the individuals
bootstrap or the values reshuffle per individual. It also allows the
construction of a consensus network, based on multiple wTO networks. The
package includes a visualization tool for the networks.  More about the
methodology can be found at <arXiv:1711.04702>.

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
