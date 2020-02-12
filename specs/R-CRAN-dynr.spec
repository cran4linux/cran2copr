%global packname  dynr
%global packver   0.1.15-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.15.25
Release:          1%{?dist}
Summary:          Dynamic Modeling in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    gsl-devel
Requires:         gsl
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-latex2exp 
Requires:         R-grid 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-car 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-deSolve 

%description
Intensive longitudinal data have become increasingly prevalent in various
scientific disciplines. Many such data sets are noisy, multivariate, and
multi-subject in nature. The change functions may also be continuous, or
continuous but interspersed with periods of discontinuities (i.e., showing
regime switches). The package 'dynr' (Dynamic Modeling in R) is an R
package that implements a set of computationally efficient algorithms for
handling a broad class of linear and nonlinear discrete- and
continuous-time models with regime-switching properties under the
constraint of linear Gaussian measurement functions. The discrete-time
models can generally take on the form of a state- space or difference
equation model. The continuous-time models are generally expressed as a
set of ordinary or stochastic differential equations. All estimation and
computations are performed in C, but users are provided with the option to
specify the model of interest via a set of simple and easy-to-learn model
specification functions in R. Model fitting can be performed using single-
subject time series data or multiple-subject longitudinal data.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/models
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
