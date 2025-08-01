%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  suRface.analytics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis and Visualization of Surface-Engineered Material Properties

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-grid 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-effectsize 
Requires:         R-stats 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-multcompView 
Requires:         R-grid 

%description
A collection of functions for statistical and multivariate analysis of
surface-related data, with a focus on antimicrobial activity and
omniphobicity. Designed to support materials scientists and researchers in
exploring structure–function relationships in surface-engineered materials
through reproducible and interpretable workflows. For more details, see Li
et al. (2021) <doi:10.1002/advs.202100368>, and Kwon et al. (2020)
<doi:10.3390/polym12081826>.

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
