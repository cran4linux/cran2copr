%global packname  solarius
%global packver   0.3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0.2
Release:          1%{?dist}
Summary:          An R Interface to SOLAR

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 

%description
SOLAR is the standard software program to perform linkage and association
mappings of the quantitative trait loci (QTLs) in pedigrees of arbitrary
size and complexity. This package allows the user to exploit the variance
component methods implemented in SOLAR. It automates such routine
operations as formatting pedigree and phenotype data. It also parses the
model output and contains summary and plotting functions for exploration
of the results. In addition, solarius enables parallel computing of the
linkage and association analyses, that makes the calculation of
genome-wide scans more efficient. See <http://solar.txbiomedgenetics.org/>
for more information about SOLAR.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
