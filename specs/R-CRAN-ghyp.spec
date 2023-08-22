%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ghyp
%global packver   1.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Hyperbolic Distribution and Its Special Cases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7
Requires:         R-core >= 2.7
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
Detailed functionality for working with the univariate and multivariate
Generalized Hyperbolic distribution and its special cases (Hyperbolic
(hyp), Normal Inverse Gaussian (NIG), Variance Gamma (VG), skewed
Student-t and Gaussian distribution). Especially, it contains fitting
procedures, an AIC-based model selection routine, and functions for the
computation of density, quantile, probability, random variates, expected
shortfall and some portfolio optimization and plotting routines as well as
the likelihood ratio test. In addition, it contains the Generalized
Inverse Gaussian distribution. See Chapter 3 of A. J. McNeil, R. Frey, and
P. Embrechts. Quantitative risk management: Concepts, techniques and
tools. Princeton University Press, Princeton (2005).

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
