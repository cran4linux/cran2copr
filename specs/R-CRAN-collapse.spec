%global packname  collapse
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced and Fast Data Transformation

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-lfe >= 2.7
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
Requires:         R-CRAN-lfe >= 2.7
Requires:         R-CRAN-Rcpp >= 1.0.1

%description
A C/C++ based package for advanced data transformation and statistical
computing in R that is extremely fast, flexible and parsimonious to code
with and programmer friendly. It is well integrated with 'dplyr', 'plm'
and 'data.table'. --- Key Features: --- (1) Advanced statistical
programming: A full set of fast statistical functions supporting grouped
and weighted computations on vectors, matrices and data frames. Fast and
programmable grouping, ordering, unique values / rows, factor generation
and interactions. Fast and flexible functions for data manipulation and
data object conversions. (2) Advanced aggregation: Fast and easy
multi-data-type, multi-function, weighted, parallelized and fully
customized data aggregation. (3) Advanced transformations: Fast (grouped)
replacing and sweeping out of statistics, and (grouped, weighted) scaling
/ standardizing, between (averaging) and (quasi-)within (centering /
demeaning) transformations, higher-dimensional centering (i.e. multiple
fixed effects transformations), linear prediction and partialling-out. (4)
Advanced time-computations: Fast (sequences of) lags / leads, and (lagged
/ leaded, iterated, quasi-, log-) differences and growth rates on
(unordered) time series and panel data. Multivariate auto-, partial- and
cross-correlation functions for panel data. Panel data to (ts-)array
conversions. (5) List processing: (Recursive) list search /
identification, extraction / subsetting, data-apply, and generalized
row-binding / unlisting in 2D. (6) Advanced data exploration: Fast
(grouped, weighted, panel-decomposed) summary statistics for complex
multilevel / panel data.

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
