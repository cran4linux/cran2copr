%global __brp_check_rpaths %{nil}
%global packname  glmmsr
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Fit a Generalized Linear Mixed Model

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-Matrix 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-numDeriv 

%description
Conduct inference about generalized linear mixed models, with a choice
about which method to use to approximate the likelihood. In addition to
the Laplace and adaptive Gaussian quadrature approximations, which are
borrowed from 'lme4', the likelihood may be approximated by the sequential
reduction approximation, or an importance sampling approximation. These
methods provide an accurate approximation to the likelihood in some
situations where it is not possible to use adaptive Gaussian quadrature.

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
%doc %{rlibdir}/%{packname}/calibration_parameters.yml
%doc %{rlibdir}/%{packname}/cluster_graph.yml
%doc %{rlibdir}/%{packname}/continuous_beliefs.yml
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/extended_family.yml
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/RcppR6.yml
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
