%global packname  riskParityPortfolio
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Design of Risk Parity Portfolios

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-alabama 
Requires:         R-Matrix 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Rcpp 

%description
Fast design of risk parity portfolios for financial investment. The goal
of the risk parity portfolio formulation is to equalize or distribute the
risk contributions of the different assets, which is missing if we simply
consider the overall volatility of the portfolio as in the mean-variance
Markowitz portfolio. In addition to the vanilla formulation, where the
risk contributions are perfectly equalized subject to no shortselling and
budget constraints, many other formulations are considered that allow for
box constraints and shortselling, as well as the inclusion of additional
objectives like the expected return and overall variance. See vignette for
a detailed documentation and comparison, with several illustrative
examples. The package is based on the papers: Y. Feng, and D. P. Palomar
(2015). SCRIP: Successive Convex Optimization Methods for Risk Parity
Portfolio Design. IEEE Trans. on Signal Processing, vol. 63, no. 19, pp.
5285-5300. <doi:10.1109/TSP.2015.2452219>. F. Spinu (2013), An Algorithm
for Computing Risk Parity Weights. <doi:10.2139/ssrn.2297383>. T.
Griveau-Billion, J. Richard, and T. Roncalli (2013). A fast algorithm for
computing High-dimensional risk parity portfolios. <arXiv:1311.4057>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
