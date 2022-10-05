%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  summclust
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Module to Compute Influence and Leverage Statistics for Regression Models with Clustered Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dreamerr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-generics 
Requires:         R-utils 
Requires:         R-CRAN-dreamerr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-generics 

%description
Module to compute cluster specific information for regression models with
clustered errors, including leverage and influence statistics. Models of
type 'lm' and 'fixest'(from the 'stats' and 'fixest' packages) are
supported. 'summclust' implements similar features as the user-written
'summclust.ado' Stata module (MacKinnon, Nielsen & Webb, 2022;
<arXiv:2205.03288v1>).

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
