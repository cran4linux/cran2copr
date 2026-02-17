%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mulSEM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Some Multivariate Analyses using Structural Equation Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-stats 
Requires:         R-CRAN-OpenMx 
Requires:         R-stats 

%description
A set of functions for some multivariate analyses utilizing a structural
equation modeling (SEM) approach through the 'OpenMx' package. These
analyses include canonical correlation analysis (CANCORR), redundancy
analysis (RDA), and multivariate principal component regression (MPCR). It
implements procedures discussed in Gu and Cheung (2023)
<doi:10.1111/bmsp.12301>, Gu, Yung, and Cheung (2019)
<doi:10.1080/00273171.2018.1512847>, and Gu et al. (2023)
<doi:10.1080/00273171.2022.2141675>.

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
