%global packname  stlplus
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Enhanced Seasonal Decomposition of Time Series by Loess

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-lattice 
Requires:         R-CRAN-yaImpute 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Decompose a time series into seasonal, trend, and remainder components
using an implementation of Seasonal Decomposition of Time Series by Loess
(STL) that provides several enhancements over the STL method in the stats
package.  These enhancements include handling missing values, providing
higher order (quadratic) loess smoothing with automated parameter choices,
frequency component smoothing beyond the seasonal and trend components,
and some basic plot methods for diagnostics.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
