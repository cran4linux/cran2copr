%global packname  loo
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          3%{?dist}
Summary:          Efficient Leave-One-Out Cross-Validation and WAIC for BayesianModels

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
Requires:         pandoc-citeproc
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats >= 0.52
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-matrixStats >= 0.52
Requires:         R-CRAN-checkmate 
Requires:         R-parallel 
Requires:         R-stats 

%description
Efficient approximate leave-one-out cross-validation (LOO) for Bayesian
models fit using Markov chain Monte Carlo, as described in Vehtari,
Gelman, and Gabry (2017) <doi:10.1007/s11222-016-9696-4>. The
approximation uses Pareto smoothed importance sampling (PSIS), a new
procedure for regularizing importance weights. As a byproduct of the
calculations, we also obtain approximate standard errors for estimated
predictive errors and for the comparison of predictive errors between
models. The package also provides methods for using stacking and other
model weighting techniques to average Bayesian predictive distributions.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
