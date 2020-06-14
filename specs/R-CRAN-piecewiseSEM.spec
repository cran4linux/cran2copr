%global packname  piecewiseSEM
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          Piecewise Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-nlme 
Requires:         R-CRAN-car 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-nlme 

%description
Implements piecewise structural equation modeling from a single list of
structural equations, with new methods for non-linear, latent, and
composite variables, standardized coefficients, query-based prediction and
indirect effects. See <http://jslefche.github.io/piecewiseSEM/> for more.

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
