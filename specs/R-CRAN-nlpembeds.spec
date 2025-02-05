%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlpembeds
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Natural Language Processing Embeddings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-rsvd 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-rsvd 

%description
Provides efficient methods to compute co-occurrence matrices, pointwise
mutual information (PMI) and singular value decomposition (SVD). In the
biomedical and clinical settings, one challenge is the huge size of
databases, e.g. when analyzing data of millions of patients over tens of
years. To address this, this package provides functions to efficiently
compute monthly co-occurrence matrices, which is the computational
bottleneck of the analysis, by using the 'RcppAlgos' package and sparse
matrices. Furthermore, the functions can be called on 'SQL' databases,
enabling the computation of co-occurrence matrices of tens of gigabytes of
data, representing millions of patients over tens of years. Partly based
on Hong C. (2021) <doi:10.1038/s41746-021-00519-z>.

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
