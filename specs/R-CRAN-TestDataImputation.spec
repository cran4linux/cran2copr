%global __brp_check_rpaths %{nil}
%global packname  TestDataImputation
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Missing Item Responses Imputation for Test and Assessment Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-Amelia 
Requires:         R-stats 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-Amelia 

%description
Functions for imputing missing item responses for dichotomous and
polytomous test and assessment data. This package enables missing
imputation methods that are suitable for test and assessment data,
including: listwise (LW) deletion (see De Ayala et al. 2001
<doi:10.1111/j.1745-3984.2001.tb01124.x>), treating as incorrect (IN, see
Lord, 1974 <doi: 10.1111/j.1745-3984.1974.tb00996.x>; Mislevy & Wu, 1996
<doi: 10.1002/j.2333-8504.1996.tb01708.x>; Pohl et al., 2014 <doi:
10.1177/0013164413504926>), person mean imputation (PM), item mean
imputation (IM), two-way (TW) and response function (RF) imputation (see
Sijtsma & van der Ark, 2003 <doi: 10.1207/s15327906mbr3804_4>), logistic
regression (LR) imputation, and expectation–maximization (EM) imputation
(see Finch, 2008 <doi: 10.1111/j.1745-3984.2008.00062.x>).

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
