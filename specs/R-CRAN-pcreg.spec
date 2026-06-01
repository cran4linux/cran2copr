%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pcreg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Advanced Methods for Principal Component Analysis and Principal Component Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-grid 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-robustbase 
Requires:         R-grid 

%description
Provides a unified framework for principal component analysis (PCA) and
principal component regression (PCR), including standard PCA, sparse PCA,
robust PCA, and supervised PCA. The package supports automatic selection
of the number of components using cumulative variance and elbow methods
and integrates PCA with regression modelling through PCR models. It
includes tools for PCA suitability assessment using Bartlett's test of
sphericity and the Kaiser-Meyer-Olkin (KMO) measure. Visualisation
utilities such as scree plots and biplots are provided for interpretation.
The methods are designed to handle multicollinearity, outliers, and
high-dimensional data, making them suitable for applied statistical
modelling and data analysis. The methodology is based on established
approaches described in Jolliffe (2002) <doi:10.1007/b98835>, Zou et al.
(2006) <doi:10.1111/j.1467-9868.2005.00503.x>, and Hubert et al. (2005)
<doi:10.1198/004017004000000563>.

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
