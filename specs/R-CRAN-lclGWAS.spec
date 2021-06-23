%global __brp_check_rpaths %{nil}
%global packname  lclGWAS
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Efficient Estimation of Discrete-Time Multivariate Frailty ModelUsing Exact Likelihood Function for Grouped Survival Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.4

%description
The core of this 'Rcpp' based package is several functions to estimate the
baseline hazard, frailty variance, and fixed effect parameter for a
discrete-time shared frailty model with random effects. The functions are
designed to analyze grouped time-to-event data accounting for family
structure of related individuals (i.e., trios). The core functions include
two processes: (1) evaluate the multivariable integration to compute the
exact proportional hazards model based likelihood and (2) estimate the
desired parameters using maximum likelihood estimation. The integration is
evaluated by the 'Cuhre' algorithm from the 'Cuba' library (Hahn, T.,
Cuba-a library for multidimensional numerical integration, Comput. Phys.
Commun. 168, 2005, 78-95 <doi:10.1016/j.cpc.2005.01.010>), and the source
files of the 'Cuhre' function are included in this package. The
maximization process is carried out using Brent's algorithm, with the
'C++' code file from John Burkardt and John Denker (Brent, R.,Algorithms
for Minimization without Derivatives, Dover, 2002, ISBN 0-486-41998-3).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
