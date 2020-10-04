%global packname  multivariance
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}%{?buildtag}
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
detect and quantify dependence of arbitrarily many random vectors. The
necessary functions are implemented in this packages and examples are
given. It includes: distance multivariance, distance multicorrelation,
dependence structure detection, tests of independence and copula versions
of distance multivariance based on the Monte Carlo empirical transform.
Detailed references are given in the package description, as starting
point for the theoretic background we refer to: B. Böttcher, Dependence
and Dependence Structures: Estimation and Visualization Using the Unifying
Concept of Distance Multivariance. Open Statistics, Vol. 1, No. 1 (2020),
<doi:10.1515/stat-2020-0001>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
