%global packname  spup
%global packver   1.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Uncertainty Propagation Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-whisker 
Requires:         R-graphics 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-whisker 

%description
Uncertainty propagation analysis in spatial environmental modelling
following methodology described in Heuvelink et al. (2007)
<doi:10.1080/13658810601063951> and Brown and Heuvelink (2007)
<doi:10.1016/j.cageo.2006.06.015>. The package provides functions for
examining the uncertainty propagation starting from input data and model
parameters, via the environmental model onto model outputs. The functions
include uncertainty model specification, stochastic simulation and
propagation of uncertainty using Monte Carlo (MC) techniques. Uncertain
variables are described by probability distributions. Both numerical and
categorical data types are handled. Spatial auto-correlation within an
attribute and cross-correlation between attributes is accommodated for.
The MC realizations may be used as input to the environmental models
called from R, or externally.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
