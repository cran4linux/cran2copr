%global packname  BNSP
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          3%{?dist}
Summary:          Bayesian Non- And Semi-Parametric Model Fitting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-threejs 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-label.switching 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-threejs 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-plyr 
Requires:         R-mgcv 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-label.switching 

%description
MCMC algorithms & processing functions for: 1. multivariate (and
univariate) regression, with nonparametric models for the means, the
variances and the correlation matrix, with variable selection, and 2.
Dirichlet process mixtures.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
