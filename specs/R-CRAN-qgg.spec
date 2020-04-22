%global packname  qgg
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Statistical Tools for Quantitative Genetic Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-MASS 
Requires:         R-CRAN-data.table 
Requires:         R-parallel 
Requires:         R-CRAN-statmod 
Requires:         R-stats 
Requires:         R-CRAN-MCMCpack 
Requires:         R-MASS 

%description
Provides an infrastructure for efficient processing of large-scale genetic
and phenotypic data including core functions for: 1) fitting linear mixed
models, 2) constructing marker-based genomic relationship matrices, 3)
estimating genetic parameters (heritability and correlation), 4)
performing genomic prediction and genetic risk profiling, and 5) single or
multi-marker association analyses. Rohde et al. (2019)
<doi:10.1101/503631>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
