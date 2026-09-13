%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  geosmooth
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Smoothing and Conditional Expectation Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-dgraphs >= 0.1.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-dgraphs >= 0.1.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides geometric methods for nonparametric regression and density
estimation on data represented as coordinate matrices or weighted graphs.
Methods include local polynomial smoothing, model-averaged local
polynomial smoothing, local polynomial lifting trend filtering,
synchronized local polynomial lifting trend filtering, graph low-pass
filtering, and Hessian-energy regression. Methodological references
include Gajer and Ravel (2025) "Adaptive Geometric Regression for
High-Dimensional Structured Data" <doi:10.48550/arXiv.2511.03817>, Fan and
Gijbels (1996, ISBN:9780412983214), Wang et al. (2016) "Trend Filtering on
Graphs" <https://www.jmlr.org/papers/v17/15-147.html>, and Kim et al.
(2009) "Semi-Supervised Regression Using Hessian Energy"
<https://papers.nips.cc/paper/3741-semi-supervised-regression-using-hessian-energy-with-an-application-to-semi-supervised-dimensionality-reduction>.

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
