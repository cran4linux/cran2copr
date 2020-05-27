%global packname  collapse
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Advanced and Fast Data Transformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-lfe >= 2.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-lfe >= 2.7
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
A C/C++ based package for advanced data transformation in R that is
extremely fast, flexible and parsimonious to code with and programmer
friendly. It is well integrated with 'dplyr', 'plm' and 'data.table'. ---
Key Features: --- (1) Advanced data programming: A full set of fast
statistical functions supporting grouped and weighted computations on
vectors, matrices and data frames. Fast (ordered) and programmable
grouping, factor generation, manipulation of data frames and data object
conversions. (2) Advanced aggregation: Fast and easy multi-data-type,
multi-function, weighted, parallelized and fully customized data
aggregation. (3) Advanced transformations: Fast (grouped, weighted)
replacing and sweeping out of statistics, scaling / standardizing,
centering (i.e. between and within transformations), higher-dimensional
centering (i.e. multiple fixed effects transformations), linear prediction
and partialling-out. (4) Advanced time-computations: Fast (sequences of)
lags / leads, and (lagged / leaded, iterated, quasi-, log-) differences
and growth rates on (unordered) time-series and panel data. Multivariate
auto, partial and cross-correlation functions for panel data. Panel data
to (ts-)array conversions. (5) List processing: (Recursive) list search /
identification, extraction / subsetting, data-apply, and generalized
row-binding / unlisting in 2D. (6) Advanced data exploration: Fast
(grouped, weighted, panel-decomposed) summary statistics for complex
multilevel / panel data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
