%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  themis
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Recipes Steps for Dealing with Unbalanced Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes >= 1.0.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROSE 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hardhat 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-recipes >= 1.0.4
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-CRAN-gower 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROSE 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hardhat 
Requires:         R-CRAN-vctrs 

%description
A dataset with an uneven number of cases in each class is said to be
unbalanced. Many models produce a subpar performance on unbalanced
datasets. A dataset can be balanced by increasing the number of minority
cases using SMOTE 2011 <arXiv:1106.1813>, BorderlineSMOTE 2005
<doi:10.1007/11538059_91> and ADASYN 2008
<https://ieeexplore.ieee.org/document/4633969>. Or by decreasing the
number of majority cases using NearMiss 2003
<https://www.site.uottawa.ca/~nat/Workshop2003/jzhang.pdf> or Tomek link
removal 1976 <https://ieeexplore.ieee.org/document/4309452>.

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
