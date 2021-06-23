%global __brp_check_rpaths %{nil}
%global packname  tolerance
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Tolerance Intervals and Regions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-stats4 
Requires:         R-MASS 
Requires:         R-CRAN-rgl 
Requires:         R-stats4 

%description
Statistical tolerance limits provide the limits between which we can
expect to find a specified proportion of a sampled population with a given
level of confidence.  This package provides functions for estimating
tolerance limits (intervals) for various univariate distributions
(binomial, Cauchy, discrete Pareto, exponential, two-parameter
exponential, extreme value, hypergeometric, Laplace, logistic, negative
binomial, negative hypergeometric, normal, Pareto, Poisson-Lindley,
Poisson, uniform, and Zipf-Mandelbrot), Bayesian normal tolerance limits,
multivariate normal tolerance regions, nonparametric tolerance intervals,
tolerance bands for regression settings (linear regression, nonlinear
regression, nonparametric regression, and multivariate regression), and
analysis of variance tolerance intervals.  Visualizations are also
available for most of these settings.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
