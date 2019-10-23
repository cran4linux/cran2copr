%global packname  gpDDE
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          General Profiling Method for Delay Differential Equation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-CollocInfer >= 1.0.2
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-TSA 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-trustOptim 
BuildRequires:    R-methods 
Requires:         R-CRAN-CollocInfer >= 1.0.2
Requires:         R-CRAN-fda 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-deSolve 
Requires:         R-MASS 
Requires:         R-CRAN-TSA 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-trustOptim 
Requires:         R-methods 

%description
Functions implement collocation-inference for stochastic process driven by
distributed delay differential equations. They also provide tools for
selecting the lags for distributed delay using shrinkage methods,
estimating time-varying coefficients, and tools for inference and
prediction.

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
%{rlibdir}/%{packname}/INDEX
