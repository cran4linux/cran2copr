%global __brp_check_rpaths %{nil}
%global packname  penPHcure
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection in PH Cure Model with Time-Varying Covariates

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-survival 
Requires:         R-CRAN-Rcpp 
Requires:         R-MASS 
Requires:         R-CRAN-Rdpack 

%description
Implementation of the semi-parametric proportional-hazards (PH) of Sy and
Taylor (2000) <doi:10.1111/j.0006-341X.2000.00227.x> extended to
time-varying covariates. Estimation and variable selection are based on
the methodology described in Beretta and Heuchenne (2019)
<doi:10.1080/02664763.2018.1554627>; confidence intervals of the parameter
estimates may be computed using a bootstrap approach. Moreover, data
following the PH cure model may be simulated using a method similar to
Hendry (2014) <doi:10.1002/sim.5945>, where the event-times are generated
on a continuous scale from a piecewise exponential distribution
conditional on time-varying covariates.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
