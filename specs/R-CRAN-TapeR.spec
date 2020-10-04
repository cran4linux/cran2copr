%global packname  TapeR
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Flexible Tree Taper Curves Based on Semiparametric Mixed Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-pracma 
Requires:         R-nlme 
Requires:         R-splines 
Requires:         R-CRAN-pracma 

%description
Implementation of functions for fitting taper curves (a semiparametric
linear mixed effects taper model) to diameter measurements along stems.
Further functions are provided to estimate the uncertainty around the
predicted curves, to calculate timber volume (also by sections) and
marginal (e.g., upper) diameters. For cases where tree heights are not
measured, methods for estimating additional variance in volume predictions
resulting from uncertainties in tree height models (tariffs) are provided.
The example data include the taper curve parameters for Norway spruce used
in the 3rd German NFI fitted to 380 trees and a subset of section-wise
diameter measurements of these trees. The functions implemented here are
detailed in the following publication: Kublin, E., Breidenbach, J.,
Kaendler, G. (2013) A flexible stem taper and volume prediction method
based on mixed-effects B-spline regression, Eur J For Res, 132:983-997.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
