%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CMHNPA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Cochran-Mantel-Haenszel and Nonparametric ANOVA

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-car 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-car 

%description
Cochran-Mantel-Haenszel methods (Cochran (1954) <doi:10.2307/3001616>;
Mantel and Haenszel (1959) <doi:10.1093/jnci/22.4.719>; Landis et al.
(1978) <doi:10.2307/1402373>) are a suite of tests applicable to
categorical data. A competitor to those tests is the procedure of
Nonparametric ANOVA which was initially introduced in Rayner and Best
(2013) <doi:10.1111/anzs.12041>. The methodology was then extended in
Rayner et al. (2015) <doi:10.1111/anzs.12113>. This package employs
functions related to both methodologies and serves as an accompaniment to
the book: An Introduction to Cochran–Mantel–Haenszel and Non-Parametric
ANOVA. The package also contains the data sets used in that text.

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
