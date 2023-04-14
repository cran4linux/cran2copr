%global __brp_check_rpaths %{nil}
%global packname  VarianceGamma
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          The Variance Gamma Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-DistributionUtils 
BuildRequires:    R-CRAN-GeneralizedHyperbolic 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-DistributionUtils 
Requires:         R-CRAN-GeneralizedHyperbolic 

%description
Provides functions for the variance gamma distribution. Density,
distribution and quantile functions. Functions for random number
generation and fitting of the variance gamma to data. Also, functions for
computing moments of the variance gamma distribution of any order about
any location. In addition, there are functions for checking the validity
of parameters and to interchange different sets of parameterizations for
the variance gamma distribution.

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
