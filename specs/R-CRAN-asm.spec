%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  asm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Convex M-Estimation for Linear Regression via Antitonic Score Matching

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quantreg 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quantreg 

%description
Performs linear regression with respect to a data-driven convex loss
function that is chosen to minimize the asymptotic covariance of the
resulting M-estimator. The convex loss function is estimated in 5 steps:
(1) form an initial OLS (ordinary least squares) or LAD (least absolute
deviation) estimate of the regression coefficients; (2) use the resulting
residuals to obtain a kernel estimator of the error density; (3) estimate
the score function of the errors by differentiating the logarithm of the
kernel density estimate; (4) compute the L2 projection of the estimated
score function onto the set of decreasing functions; (5) take a negative
antiderivative of the projected score function estimate. Newton's method
(with Hessian modification) is then used to minimize the convex empirical
risk function. Further details of the method are given in Feng et al.
(2024) <doi:10.48550/arXiv.2403.16688>.

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
