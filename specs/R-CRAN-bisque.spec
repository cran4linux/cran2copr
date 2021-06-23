%global __brp_check_rpaths %{nil}
%global packname  bisque
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Inference via Sparse Grid QuadratureEvaluation (BISQuE) for Hierarchical Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-mvQuad 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mvQuad 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-itertools 

%description
Implementation of the 'bisque' strategy for approximate Bayesian posterior
inference.  See Hewitt and Hoeting (2019) <arXiv:1904.07270> for complete
details.  'bisque' combines conditioning with sparse grid quadrature rules
to approximate marginal posterior quantities of hierarchical Bayesian
models.  The resulting approximations are computationally efficient for
many hierarchical Bayesian models.  The 'bisque' package allows
approximate posterior inference for custom models; users only need to
specify the conditional densities required for the approximation.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
