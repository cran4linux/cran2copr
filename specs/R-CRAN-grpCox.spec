%global packname  grpCox
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Penalized Cox Model for High-Dimensional Data with GroupedPredictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix >= 1.2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-Matrix >= 1.2.10
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-MASS 
Requires:         R-CRAN-colorspace 

%description
Fit the penalized Cox models with both non-overlapping and overlapping
grouped penalties including the group lasso, group smoothly clipped
absolute deviation (SCAD), and group minimax concave penalty (MCP). The
algorithms combine the Majorization Minimization (MM) approach and
group-wise descent with some computational tricks including the screening,
active set, and warm-start. Different tuning regularization parameter
methods are provided.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
