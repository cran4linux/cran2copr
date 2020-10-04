%global packname  GB2
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Beta Distribution of the Second Kind: Properties,Likelihood, Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-CRAN-survey 

%description
Package GB2 explores the Generalized Beta distribution of the second kind.
Density, cumulative distribution function, quantiles and moments of the
distributions are given. Functions for the full log-likelihood, the
profile log-likelihood and the scores are provided. Formulas for various
indicators of inequality and poverty under the GB2 are implemented. The
GB2 is fitted by the methods of maximum pseudo-likelihood estimation using
the full and profile log-likelihood, and non-linear least squares
estimation of the model parameters. Various plots for the visualization
and analysis of the results are provided. Variance estimation of the
parameters is provided for the method of maximum pseudo-likelihood
estimation. A mixture distribution based on the compounding property of
the GB2 is presented (denoted as "compound" in the documentation). This
mixture distribution is based on the discretization of the distribution of
the underlying random scale parameter. The discretization can be left or
right tail. Density, cumulative distribution function, moments and
quantiles for the mixture distribution are provided. The compound mixture
distribution is fitted using the method of maximum pseudo-likelihood
estimation. The fit can also incorporate the use of auxiliary information.
In this new version of the package, the mixture case is complemented with
new functions for variance estimation by linearization and comparative
density plots.

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
