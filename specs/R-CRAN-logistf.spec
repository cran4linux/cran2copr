%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logistf
%global packver   1.26.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.26.1
Release:          1%{?dist}%{?buildtag}
Summary:          Firth's Bias-Reduced Logistic Regression

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-Matrix 

%description
Fit a logistic regression model using Firth's bias reduction method,
equivalent to penalization of the log-likelihood by the Jeffreys prior.
Confidence intervals for regression coefficients can be computed by
penalized profile likelihood. Firth's method was proposed as ideal
solution to the problem of separation in logistic regression, see Heinze
and Schemper (2002) <doi:10.1002/sim.1047>. If needed, the bias reduction
can be turned off such that ordinary maximum likelihood logistic
regression is obtained. Two new modifications of Firth's method, FLIC and
FLAC, lead to unbiased predictions and are now available in the package as
well, see Puhr et al (2017) <doi:10.1002/sim.7273>.

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
