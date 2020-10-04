%global packname  warpMix
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Mixed Effects Modeling with Warping for Functional Data UsingB-Spline

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 8.4
BuildRequires:    R-MASS >= 7.3.44
BuildRequires:    R-nlme >= 3.1.128
BuildRequires:    R-CRAN-fda >= 2.4.4
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-lme4 >= 1.1.12
Requires:         R-CRAN-fields >= 8.4
Requires:         R-MASS >= 7.3.44
Requires:         R-nlme >= 3.1.128
Requires:         R-CRAN-fda >= 2.4.4
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-lme4 >= 1.1.12

%description
Mixed effects modeling with warping for functional data using B- spline.
Warping coefficients are considered as random effects, and warping
functions are general functions, parameters representing the projection
onto B- spline basis of a part of the warping functions. Warped data are
modelled by a linear mixed effect functional model, the noise is Gaussian
and independent from the warping functions.

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
