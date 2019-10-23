%global packname  multivariance
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Measuring Multivariate Dependence Using Distance Multivariance

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-microbenchmark 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-microbenchmark 

%description
Distance multivariance is a measure of dependence which can be used to
detect and quantify dependence. The necessary functions are implemented in
this packages, and examples are given. For the theoretic background we
refer to the papers: B. Böttcher, Dependence and Dependence Structures:
Estimation and Visualization Using Distance Multivariance.
<arXiv:1712.06532>. B. Böttcher, M. Keller-Ressel, R.L. Schilling,
Detecting independence of random vectors: generalized distance covariance
and Gaussian covariance. VMSTA, 2018, Vol. 5, No. 3, 353-383.
<arXiv:1711.07778>. B. Böttcher, M. Keller-Ressel, R.L. Schilling,
Distance multivariance: New dependence measures for random vectors.
<arXiv:1711.07775>. G. Berschneider, B. Böttcher, On complex Gaussian
random fields, Gaussian quadratic forms and sample distance multivariance.
<arXiv:1808.07280>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
