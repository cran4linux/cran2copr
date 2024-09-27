%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  switchSelection
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Endogenous Switching and Sample Selection Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-hpa >= 1.3.1
BuildRequires:    R-CRAN-mnorm >= 1.2.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-gena >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-hpa >= 1.3.1
Requires:         R-CRAN-mnorm >= 1.2.1
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-gena >= 1.0.0
Requires:         R-methods 

%description
Estimate the parameters of multivariate endogenous switching and sample
selection models using methods described in Newey (2009)
<doi:10.1111/j.1368-423X.2008.00263.x>, E. Kossova, B. Potanin (2018)
<https://ideas.repec.org/a/ris/apltrx/0346.html>, E. Kossova, L.
Kupriianova, B. Potanin (2020)
<https://ideas.repec.org/a/ris/apltrx/0391.html> and E. Kossova, B.
Potanin (2022) <https://ideas.repec.org/a/ris/apltrx/0455.html>.

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
