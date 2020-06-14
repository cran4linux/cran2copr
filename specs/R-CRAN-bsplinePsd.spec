%global packname  bsplinePsd
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}
Summary:          Bayesian Nonparametric Spectral Density Estimation UsingB-Spline Priors

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-splines >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
Requires:         R-splines >= 3.2.3
Requires:         R-CRAN-Rcpp >= 0.12.5

%description
Implementation of a Metropolis-within-Gibbs MCMC algorithm to flexibly
estimate the spectral density of a stationary time series.  The algorithm
updates a nonparametric B-spline prior using the Whittle likelihood to
produce pseudo-posterior samples and is based on the work presented in
Edwards, M.C., Meyer, R. and Christensen, N., Statistics and Computing
(2018). <doi.org/10.1007/s11222-017-9796-9>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
