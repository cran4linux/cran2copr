%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDShOP
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Shrinkage Optimal Portfolios

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rdpack 

%description
Constructs shrinkage estimators of high-dimensional mean-variance
portfolios and performs high-dimensional tests on optimality of a given
portfolio. The techniques developed in Bodnar et al. (2018)
<doi:10.1016/j.ejor.2017.09.028>, Bodnar et al. (2019)
<doi:10.1109/TSP.2019.2929964>, Bodnar et al. (2020)
<doi:10.1109/TSP.2020.3037369> are central to the package. They provide
simple and feasible estimators and tests for optimal portfolio weights,
which are applicable for 'large p and large n' situations where p is the
portfolio dimension (number of stocks) and n is the sample size. The
package also includes tools for constructing portfolios based on shrinkage
estimators of the mean vector and covariance matrix as well as a new
Bayesian estimator for the Markowitz efficient frontier recently developed
by Bauder et al. (2021) <doi:10.1080/14697688.2020.1748214>.

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
