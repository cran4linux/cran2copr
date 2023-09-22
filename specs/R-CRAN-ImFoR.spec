%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImFoR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Linear Height Diameter Models for Forestry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-ggplot2 

%description
Tree height is an important dendrometric variable and forms the basis of
vertical structure of a forest stand. This package will help to fit and
validate various non-linear height diameter models for assessing the
underlying relationship that exists between tree height and diameter at
breast height in case of conifer trees. This package has been implemented
on Naslund, Curtis, Michailoff, Meyer, Power, Michaelis-Menten and Wykoff
non linear models using algorithm of Huang et al.  (1992)
<doi:10.1139/x92-172> and Zeide et al. (1993)
<doi:10.1093/forestscience/39.3.594>.

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
