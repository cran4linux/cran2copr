%global packname  shrinkTVP
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Efficient Bayesian Inference for Time-Varying Parameter Modelswith Shrinkage

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-GIGrvg 
BuildRequires:    R-CRAN-stochvol 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-GIGrvg 
Requires:         R-CRAN-stochvol 
Requires:         R-CRAN-coda 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
Efficient Markov chain Monte Carlo (MCMC) algorithms for fully Bayesian
estimation of time-varying parameter models with shrinkage priors. Details
on the algorithms used are provided in Bitto and Frühwirth-Schnatter
(2019) <doi:10.1016/j.jeconom.2018.11.006>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
