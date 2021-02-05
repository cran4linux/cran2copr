%global packname  RXshrink
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
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
for a wide variety of alternative shrinkage Paths. While all methods focus
on Maximum Likelihood estimation of unknown true effects under
Normal-distribution theory, some estimates are modified to be Unbiased or
to have "Correct Range" when estimating either [1] the noncentrality of
the F-ratio for testing that true Beta coefficients are Zeros or [2] the
"relative" MSE Risk (i.e. MSE divided by true sigma-square, where the
"relative" variance of OLS is known.) The unr.ridge() function implements
the "Unrestricted Path" introduced in Obenchain (2020) <arXiv:2005.14291>.
This "new" p-parameter Shrinkage-Path and that of eff.ridge() are both
more efficient than the Paths used by qm.ridge(), aug.lars() and
uc.lars(). Functions eff.aug() and eff.biv() augment the calculations made
by eff.ridge() to provide plots of the bivariate confidence ellipses
corresponding to any of the p*(p-1) possible pairs of shrunken regression
coefficients.

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
