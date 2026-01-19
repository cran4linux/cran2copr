%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eigenmodel
%global packver   1.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.12
Release:          1%{?dist}%{?buildtag}
Summary:          Semiparametric Factor and Regression Models for Symmetric Relational Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Estimation of the parameters in a model for symmetric relational data
(e.g., the above-diagonal part of a square matrix), using a model-based
eigenvalue decomposition and regression. Missing data is accommodated, and
a posterior mean for missing data is calculated under the assumption that
the data are missing at random. The marginal distribution of the
relational data can be arbitrary, and is fit with an ordered probit
specification. See Hoff (2007) <doi:10.48550/arXiv.0711.1146>. for details
on the model.

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
