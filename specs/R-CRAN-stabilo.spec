%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stabilo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stabilometric Signal Quantification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-pracma 
Requires:         R-stats 

%description
Functions for stabilometric signal quantification. The input is a data
frame containing the x, y coordinates of the center-of-pressure
displacement. Jose Magalhaes de Oliveira (2017)
<doi:10.3758/s13428-016-0706-4> "Statokinesigram normalization method"; T
E Prieto, J B Myklebust, R G Hoffmann, E G Lovett, B M Myklebust (1996)
<doi:10.1109/10.532130> "Measures of postural steadiness: Differences
between healthy young and elderly adults"; L F Oliveira et al (1996)
<doi:10.1088/0967-3334/17/4/008> "Calculation of area of stabilometric
signals using principal component analisys".

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
