%global packname  lspartition
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Nonparametric Estimation and Inference Procedures usingPartitioning-Based Least Squares Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-mgcv 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-matrixStats 
Requires:         R-MASS 
Requires:         R-CRAN-dplyr 

%description
Tools for statistical analysis using partitioning-based least squares
regression as described in Cattaneo, Farrell and Feng (2019a,
<arXiv:1804.04916>) and Cattaneo, Farrell and Feng (2019b,
<arXiv:1906.00202>): lsprobust() for nonparametric point estimation of
regression functions and their derivatives and for robust bias-corrected
(pointwise and uniform) inference; lspkselect() for data-driven selection
of the IMSE-optimal number of knots; lsprobust.plot() for regression plots
with robust confidence intervals and confidence bands; lsplincom() for
estimation and inference for linear combinations of regression functions
from different groups.

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
%{rlibdir}/%{packname}/INDEX
