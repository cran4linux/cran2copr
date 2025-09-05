%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CondMVT
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Multivariate t Distribution, Expectation Maximization Algorithm, and Its Stochastic Variants

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 

%description
Computes conditional multivariate t probabilities, random deviates, and
densities. It can also be used to create missing values at random in a
dataset, resulting in a missing at random (MAR) mechanism. Inbuilt in the
package are the Expectation-Maximization (EM), Monte Carlo EM, and
Stochastic EM algorithms for imputation of missing values in datasets
assuming the multivariate t distribution. See Kinyanjui, Tamba, Orawo, and
Okenye (2020)<doi:10.3233/mas-200493>, and Kinyanjui, Tamba, and
Okenye(2021)<http://www.ceser.in/ceserp/index.php/ijamas/article/view/6726/0>
for more details.

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
