%global packname  qgg
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          2%{?dist}%{?buildtag}
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
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
