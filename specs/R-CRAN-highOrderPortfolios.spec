%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  highOrderPortfolios
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Design of High-Order Portfolios Including Skewness and Kurtosis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-fitHeavyTail >= 0.1.4
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-fitHeavyTail >= 0.1.4
Requires:         R-CRAN-ECOSolveR 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-quadprog 
Requires:         R-stats 
Requires:         R-utils 

%description
The classical Markowitz's mean-variance portfolio formulation ignores
heavy tails and skewness. High-order portfolios use higher order moments
to better characterize the return distribution. Different formulations and
fast algorithms are proposed for high-order portfolios based on the mean,
variance, skewness, and kurtosis. The package is based on the papers: R.
Zhou and D. P. Palomar (2021). "Solving High-Order Portfolios via
Successive Convex Approximation Algorithms." <arXiv:2008.00863>. X. Wang,
R. Zhou, J. Ying, and D. P. Palomar (2022). "Efficient and Scalable
High-Order Portfolios Design via Parametric Skew-t Distribution."
<arXiv:2206.02412>.

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
