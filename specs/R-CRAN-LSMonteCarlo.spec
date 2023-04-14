%global __brp_check_rpaths %{nil}
%global packname  LSMonteCarlo
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          American options pricing with Least Squares Monte Carlo method

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fBasics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
The package compiles functions for calculating prices of American put
options with Least Squares Monte Carlo method. The option types are plain
vanilla American put, Asian American put, and Quanto American put. The
pricing algorithms include variance reduction techniques such as
Antithetic Variates and Control Variates. Additional functions are given
to derive "price surfaces" at different volatilities and strikes, create
3-D plots, quickly generate Geometric Brownian motion, and calculate
prices of European options with Black & Scholes analytical solution.

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
