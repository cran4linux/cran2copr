%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diagL1
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Routines for Fit, Inference and Diagnostics in Linear L1 Models

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-greekLetters 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-conquer 
BuildRequires:    R-CRAN-lawstat 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-greekLetters 
Requires:         R-stats 
Requires:         R-CRAN-conquer 
Requires:         R-CRAN-lawstat 

%description
Diagnostics for linear L1 regression (also known as LAD - Least Absolute
Deviations), including: estimation, confidence intervals, tests of
hypotheses, measures of leverage, methods of diagnostics for L1
regression, special diagnostics graphs and measures of leverage. The
algorithms are based in Dielman (2005) <doi:10.1080/0094965042000223680>,
Elian et al. (2000) <doi:10.1080/03610920008832518> and Dodge (1997)
<doi:10.1006/jmva.1997.1666>. This package builds on the 'quantreg'
package, which is a well-established package for tuning quantile
regression models. There are also tests to verify if the errors have a
Laplace distribution based on the work of Puig and Stephens (2000)
<doi:10.2307/1270952>.

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
