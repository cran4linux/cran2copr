%global packname  picasso
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Pathwise Calibrated Sparse Shooting Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Computationally efficient tools for fitting generalized linear model with
convex or non-convex penalty. Users can enjoy the superior statistical
property of non-convex penalty such as SCAD and MCP which has
significantly less estimation error and overfitting compared to convex
penalty such as lasso and ridge. Computation is handled by multi-stage
convex relaxation and the PathwIse CAlibrated Sparse Shooting algOrithm
(PICASSO) which exploits warm start initialization, active set updating,
and strong rule for coordinate preselection to boost computation, and
attains a linear convergence to a unique sparse local optimum with optimal
statistical properties. The computation is memory-optimized using the
sparse matrix output.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
