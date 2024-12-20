%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  restriktor
%global packver   0.6-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Restricted Statistical Estimation and Inference for Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.10
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-norm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-lavaan >= 0.6.10
Requires:         R-CRAN-boot 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-norm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 

%description
Allow for easy-to-use testing or evaluating of linear equality and
inequality restrictions about parameters and effects in (generalized)
linear statistical models.

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
