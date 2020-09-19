%global packname  mvGPS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference using Multivariate Generalized Propensity Score

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-WeightIt 
BuildRequires:    R-CRAN-cobalt 
BuildRequires:    R-CRAN-matrixNormal 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-CBPS 
Requires:         R-CRAN-Rdpack 
Requires:         R-MASS 
Requires:         R-CRAN-WeightIt 
Requires:         R-CRAN-cobalt 
Requires:         R-CRAN-matrixNormal 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-CBPS 

%description
Methods for estimating weights and generalized propensity score for
multiple continuous exposures via the generalized propensity score
described in Williams, J.R, and Cresi, C.M (2020) <arxiv:2008.13767>.
Weights are constructed assuming an underlying multivariate normal density
for the marginal and conditional distribution of exposures given a set of
confounders. These weights can then be used to estimate dose-response
curves or surfaces. This method achieves balance across all exposure
dimension rather than along a single dimension.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
