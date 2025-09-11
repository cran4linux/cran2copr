%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  robustT2
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Hotelling-Type T² Control Chart Based on the Dual STATIS Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-Matrix 

%description
Implements a robust multivariate control-chart methodology for batch-based
industrial processes with multiple correlated variables using the Dual
STATIS (Structuration des Tableaux A Trois Indices de la Statistique)
framework. A robust compromise covariance matrix is constructed from Phase
I batches with the Minimum Covariance Determinant (MCD) estimator, and a
Hotelling-type T² statistic is applied for anomaly detection in Phase II.
The package includes functions to simulate clean and contaminated batches,
to compute both robust and classical Hotelling T² control charts, to
visualize results via robust biplots, and to launch an interactive 'shiny'
dashboard. An internal dataset (pharma_data) is provided for
reproducibility. See Lavit, Escoufier, Sabatier and Traissac (1994)
<doi:10.1016/0167-9473(94)90134-1> for the original STATIS methodology,
and Rousseeuw and Van Driessen (1999) <doi:10.1080/00401706.1999.10485670>
for the MCD estimator.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
