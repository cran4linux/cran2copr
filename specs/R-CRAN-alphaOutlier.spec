%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alphaOutlier
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Obtain Alpha-Outlier Regions for Well-Known Probability Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-quantreg 
Requires:         R-graphics 
Requires:         R-stats 

%description
Given the parameters of a distribution, the package uses the concept of
alpha-outliers by Davies and Gather (1993) to flag outliers in a data set.
See Davies, L.; Gather, U. (1993): The identification of multiple
outliers, JASA, 88 423, 782-792, <doi:10.1080/01621459.1993.10476339> for
details.

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
