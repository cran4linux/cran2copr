%global packname  BMTAR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Bayesian Approach for MTAR Models with Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-MASS 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 

%description
Implements parameter estimation using a Bayesian approach for Multivariate
Threshold Autoregressive (MTAR) models with missing data using Markov
Chain Monte Carlo methods. Performs the simulation of MTAR processes
(mtarsim()), estimation of matrix parameters and the threshold values
(mtarns()), identification of the autoregressive orders using Bayesian
variable selection (mtarstr()), identification of the number of regimes
using Metropolised Carlin and Chib (mtarnumreg()) and estimate missing
data, coefficients and covariance matrices conditional on the
autoregressive orders, the threshold values and the number of regimes
(mtarmissing()). Calderon and Nieto (2017)
<doi:10.1080/03610926.2014.990758>.

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
%{rlibdir}/%{packname}/INDEX
