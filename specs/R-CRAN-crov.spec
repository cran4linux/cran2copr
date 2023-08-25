%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crov
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Regression Model for an Ordinal Response and Ordinal Predictors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.5.0
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-CRAN-VGAM >= 1.0.5
Requires:         R-CRAN-gtools >= 3.5.0
Requires:         R-stats >= 3.4.3
Requires:         R-CRAN-VGAM >= 1.0.5

%description
Fits a constrained regression model for an ordinal response with ordinal
predictors and possibly others, Espinosa and Hennig (2019)
<DOI:10.1007/s11222-018-9842-2>. The parameter estimates associated with
an ordinal predictor are constrained to be monotonic. If a monotonicity
direction (isotonic or antitonic) is not specified for an ordinal
predictor by the user, then one of the available methods will either
establish it or drop the monotonicity assumption. Two monotonicity tests
are also available to test the null hypothesis of monotonicity over a set
of parameters associated with an ordinal predictor.

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
