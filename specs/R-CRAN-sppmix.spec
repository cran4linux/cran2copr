%global packname  sppmix
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Modeling Spatial Poisson and Related Point Processes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-mvtnorm 

%description
Implements classes and methods for modeling spatial point patterns using
inhomogeneous Poisson point processes, where the intensity surface is
assumed to be analogous to a finite additive mixture of normal components
and the number of components is a finite, fixed or random integer.
Extensions to the marked inhomogeneous Poisson point processes case are
also presented. We provide an extensive suite of R functions that can be
used to simulate, visualize and model point patterns, estimate the
parameters of the models, assess convergence of the algorithms and perform
model selection and checking in the proposed modeling context.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
