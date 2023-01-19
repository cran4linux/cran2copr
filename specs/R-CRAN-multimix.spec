%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multimix
%global packver   1.0-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Mixture Models Using the Expectation Maximisation (EM) Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 

%description
A set of functions which use the Expectation Maximisation (EM) algorithm
(Dempster, A. P., Laird, N. M., and Rubin, D. B. (1977)
<doi:10.1111/j.2517-6161.1977.tb01600.x> Maximum likelihood from
incomplete data via the EM algorithm, Journal of the Royal Statistical
Society, 39(1), 1--22) to take a finite mixture model approach to
clustering. The package is designed to cluster multivariate data that have
categorical and continuous variables and that possibly contain missing
values. The method is described in Hunt, L. and Jorgensen, M. (1999)
<doi:10.1111/1467-842X.00071> Australian & New Zealand Journal of
Statistics 41(2), 153--171 and Hunt, L. and Jorgensen, M. (2003)
<doi:10.1016/S0167-9473(02)00190-1> Mixture model clustering for mixed
data with missing information, Computational Statistics & Data Analysis,
41(3-4), 429--440.

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
