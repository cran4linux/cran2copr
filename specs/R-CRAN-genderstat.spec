%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genderstat
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Analysis Tools for Gender Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 

%description
Provides tools for quantitative analysis in gender studies, including
functions to calculate various gender inequality metrics such as the
Gender Pay Gap, Gender Inequality Index (GII), Gender Development Index
(GDI), and Gender Empowerment Measure (GEM). Also includes extracted real
datasets for practice and learning purposes, which were obtained from the
UNDP Human Development Reports Data Center
<https://hdr.undp.org/data-center/documentation-and-downloads> and the
World Bank Gender Data Portal
<https://genderdata.worldbank.org/indicators/>. References: Miller, Kevin;
Vagins, Deborah J. (2021) <https://eric.ed.gov/?id=ED596219>. Jacques
Charmes & Saskia Wieringa (2003) <doi:10.1080/1464988032000125773>. Gaëlle
Ferrant (2010) <https://shs.hal.science/halshs-00462463/>.

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
