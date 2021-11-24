%global __brp_check_rpaths %{nil}
%global packname  GhostKnockoff
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Knockoff Inference Using Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-Rdsdp 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-seqminer 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-Rdsdp 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-seqminer 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-corpcor 

%description
Functions for multiple knockoff inference using summary statistics, e.g.
Z-scores. The knockoff inference is a general procedure for controlling
the false discovery rate (FDR) when performing variable selection. This
package provides a procedure which performs knockoff inference without
ever constructing individual knockoffs (GhostKnockoff). It additionally
supports multiple knockoff inference for improved stability and
reproducibility. Moreover, it supports meta-analysis of multiple
overlapping studies.

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
