%global packname  TCA
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tensor Composition Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-config 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rsvd 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Matrix 

%description
Tensor Composition Analysis (TCA) allows the deconvolution of
two-dimensional data (features by observations) coming from a mixture of
heterogeneous sources into a three-dimensional matrix of signals (features
by observations by sources). The TCA framework further allows to test the
features in the data for different statistical relations with an outcome
of interest while modeling source-specific effects; particularly, it
allows to look for statistical relations between source-specific signals
and an outcome. For example, TCA can deconvolve bulk tissue-level DNA
methylation data (methylation sites by individuals) into a
three-dimensional tensor of cell-type-specific methylation levels for each
individual (i.e. methylation sites by individuals by cell types) and it
allows to detect cell-type-specific statistical relations (associations)
with phenotypes. For more details see Rahmani et al. (2019)
<DOI:10.1038/s41467-019-11052-9>.

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
