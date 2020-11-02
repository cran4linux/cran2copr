%global packname  RXshrink
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Likelihood Shrinkage using Generalized Ridge or Least Angle Regression Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-ellipse 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-ellipse 

%description
Functions are provided to calculate and display ridge TRACE diagnostics
for a variety of shrinkage Paths. TRACEs identify the m-Extent of
shrinkage most likely, under Normal-theory, to produce optimally biased
estimates of beta-coefficients with minimum MSE Risk. The unr.ridge()
function implements the "Unrestricted Path" introduced in Obenchain (2020)
<arXiv:2005.14291>. This Shrinkage-Path is more efficient than the Paths
used by the qm.ridge(), aug.lars() and uc.lars() functions. Optimally
biased predictions can be made using RXpredict() for all six types of
RXshrink linear model estimation methods. Functions MLboot(), MLcalc(),
MLhist() and MLtrue() provide insights into the true bias and MSE risk
characteristics of non-linear Shrinkage estimators. Functions unr.aug()
and unr.biv() augment the calculations made by unr.ridge() to provide
plots of the bivariate confidence ellipses corresponding to any of the
p*(p-1) possible pairs of shrunken regression coefficients. The
correct.signs() function provides estimates with "correct" numerical signs
when ill-conditioned (nearly multicollinear) models yield OLS estimates
that disagree with the signs of the observed correlations between the
y-outcome and the selected x-predictor variables.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
