%global packname  TCA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Tensor Composition Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-config 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-config 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-gmodels 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rsvd 
Requires:         R-stats 
Requires:         R-CRAN-quadprog 

%description
Tensor Composition Analysis (TCA) allows the deconvolution of
two-dimensional data (features by observations) coming from a mixture of
sources into a three-dimensional matrix of signals (features by
observations by sources). TCA further allows to test the features in the
data for different statistical relations with an outcome of interest while
modeling source-specific effects (TCA regression); particularly, it allows
to look for statistical relations between source-specific signals and an
outcome. For example, TCA can deconvolve bulk tissue-level DNA methylation
data (methylation sites by individuals) into a tensor of
cell-type-specific methylation levels for each individual (methylation
sites by individuals by cell types) and it allows to detect
cell-type-specific relations (associations) with an outcome of interest.
For more details see Rahmani et al. (2018) <DOI:10.1101/437368>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
