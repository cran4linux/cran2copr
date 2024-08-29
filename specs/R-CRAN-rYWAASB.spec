%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rYWAASB
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneous Selection of Trait and WAASB Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 

%description
Proposes a new ranking algorithm that utilizes a "Y*WAASB" biplot
generated from the 'metan' package. The aim of the package is to
effectively distinguish the top-ranked genotypes. For a detailed
explanation of the process of obtaining a "Y*WAASB" biplot and the related
data, please refer to the manual included in this package as well as the
study by Olivoto & Lúcio (2020) <doi:10.1111/2041-210X.13384>. In this
context, "WAASB" refers to the "Weighted Average of Absolute Scores"
provided by Olivoto et al. (2019) <doi:10.2134/agronj2019.03.0220>, which
quantifies the stability of genotypes across different environments using
linear mixed-effect models. In order to run the package, it is necessary
to extract the "WAASB" coefficients using the 'metan' package.

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
