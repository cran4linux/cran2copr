%global packname  GWmodel
%global packver   2.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          2%{?dist}
Summary:          Geographically-Weighted Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-maptools >= 0.5.2
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-spatialreg 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-maptools >= 0.5.2
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-spatialreg 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-FNN 

%description
Techniques from a particular branch of spatial statistics,termed
geographically-weighted (GW) models. GW models suit situations when data
are not described well by some global model, but where there are spatial
regions where a suitably localised calibration provides a better
description. 'GWmodel' includes functions to calibrate: GW summary
statistics (Brunsdon et al. 2002)<doi: 10.1016/s0198-9715(01)00009-6>, GW
principal components analysis (Harris et al. 2011)<doi:
10.1080/13658816.2011.554838>, GW discriminant analysis (Brunsdon et al.
2007)<doi: 10.1111/j.1538-4632.2007.00709.x> and various forms of GW
regression (Brunsdon et al. 1996)<doi:
10.1111/j.1538-4632.1996.tb00936.x>; some of which are provided in basic
and robust (outlier resistant) forms.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
