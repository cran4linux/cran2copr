%global packname  lctools
%global packver   0.2-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          Local Correlation, Spatial Inequalities, Geographically WeightedRegression and Other Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.51.3
BuildRequires:    R-CRAN-pscl >= 1.5.2
BuildRequires:    R-CRAN-weights >= 1.0
BuildRequires:    R-CRAN-reshape >= 0.8.8
Requires:         R-MASS >= 7.3.51.3
Requires:         R-CRAN-pscl >= 1.5.2
Requires:         R-CRAN-weights >= 1.0
Requires:         R-CRAN-reshape >= 0.8.8

%description
Provides researchers and educators with easy-to-learn user friendly tools
for calculating key spatial statistics and to apply simple as well as
advanced methods of spatial analysis in real data. These include: Local
Pearson and Geographically Weighted Pearson Correlation Coefficients,
Spatial Inequality Measures (Gini, Spatial Gini, LQ, Focal LQ), Spatial
Autocorrelation (Global and Local Moran's I), several Geographically
Weighted Regression techniques and other Spatial Analysis tools (other
geographically weighted statistics). This package also contains functions
for measuring the significance of each statistic calculated, mainly based
on Monte Carlo simulations.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
