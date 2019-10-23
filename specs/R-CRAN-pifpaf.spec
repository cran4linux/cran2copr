%global packname  pifpaf
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Potential Impact Fraction and Population Attributable Fractionfor Cross-Sectional Data

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.1
Requires:         R-core >= 3.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixcalc 
Requires:         R-MASS 
Requires:         R-CRAN-sfsmisc 
Requires:         R-stats 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-numDeriv 

%description
Uses a generalized method to estimate the Potential Impact Fraction (PIF)
and the Population Attributable Fraction (PAF) from cross-sectional data.
It creates point-estimates, confidence intervals, and estimates of
variance. In addition it generates plots for conducting sensitivity
analysis. The estimation method corresponds to Zepeda-Tello,
Camacho-García-Formentí, et al. 2017. 'Nonparametric Methods to Estimate
the Potential Impact Fraction from Cross-sectional Data'. Unpublished
manuscript. This package was developed under funding by Bloomberg
Philanthropies.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
