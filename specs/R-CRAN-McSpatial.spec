%global packname  McSpatial
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric spatial data analysis

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-locfit 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-SparseM 
Requires:         R-lattice 
Requires:         R-CRAN-locfit 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-SparseM 

%description
Locally weighted regression, semiparametric and conditionally parametric
regression, fourier and cubic spline functions, GMM and linearized spatial
logit and probit, k-density functions and counterfactuals, nonparametric
quantile regression and conditional density functions, Machado-Mata
decomposition for quantile regressions, spatial AR model, repeat sales
models, conditionally parametric logit and probit

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
%doc %{rlibdir}/%{packname}/maps
%{rlibdir}/%{packname}/INDEX
