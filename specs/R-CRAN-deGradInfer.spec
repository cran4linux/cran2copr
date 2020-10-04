%global packname  deGradInfer
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Parameter Inference for Systems of Differential Equation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gptk 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gptk 
Requires:         R-graphics 
Requires:         R-stats 

%description
Efficient Bayesian parameter inference for systems of ordinary
differential equations. The inference is based on adaptive gradient
matching (AGM, Dondelinger et al. 2013
<http://proceedings.mlr.press/v31/dondelinger13a.pdf>, Macdonald 2017
<http://theses.gla.ac.uk/7987/1/2017macdonaldphd.pdf>), which offers
orders-of-magnitude improvements in computational efficiency over standard
methods that require solving the differential equation system. Features of
the package include flexible specification of custom ODE systems as R
functions, support for missing variables, Bayesian inference via
population MCMC.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
