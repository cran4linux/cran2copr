%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RAMpath
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structural Equation Modeling Using the Reticular Action Model (RAM) Notation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-MASS 

%description
We rewrite of RAMpath software developed by John McArdle and Steven Boker
as an R package. In addition to performing regular SEM analysis through
the R package lavaan, RAMpath has unique features.  First, it can generate
path diagrams according to a given model. Second, it can display path
tracing rules through path diagrams and decompose total effects into their
respective direct and indirect effects as well as decompose variance and
covariance into individual bridges. Furthermore, RAMpath can fit dynamic
system models automatically based on latent change scores and generate
vector field plots based upon results obtained from a bivariate dynamic
system. Starting version 0.4, RAMpath can conduct power analysis for both
univariate and bivariate latent change score models.

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
