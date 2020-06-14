%global packname  ipptoolbox
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          IPP Toolbox

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-AlgDesign 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-kolmim 
Requires:         R-CRAN-AlgDesign 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-kolmim 

%description
Uncertainty quantification and propagation in the framework of
Dempster-Shafer Theory and imprecise probabilities. This toolbox offers
easy-to-use methods for using imprecise probabities for applied
uncertainty modelling and simulation. The package comprises the basic
functionality needed, with usability similar to standard probabilistic
analysis: - Fit imprecise probability distributions from data, - Define
imprecise probabilities based on distribution functions, - Combine with
various aggregation rules (e. g. Dempster's rule), - Plotting tools, -
Propagate through arbitrary functions / simulations via Monte Carlo, -
Perform sensitivity analyses with imprecise distributions, - Example
models for a quick start.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
