%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ModToppLeone
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modified Topp-Leone Distribution: Properties, Estimation, and Applications

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
Provides density, cumulative distribution function, quantile function,
random number generation, survival function, hazard rate function,
statistical properties, classical point and interval estimation (maximum
likelihood, ordinary least squares, weighted least squares, Cramer-von
Mises, and maximum product of spacings), Bayesian estimation under
symmetric and asymmetric loss functions (squared error, entropy,
precautionary, and generalized entropy loss functions) with highest
posterior density intervals, censoring schemes (random, Type-I, Type-II,
and progressive Type-II censoring), and real data applications for the
'Modified Topp-Leone' distribution. Methods are based on Singh et al.
(2025) <https://statassoc.or.th>, Cheng and Amin (1983)
<doi:10.1111/j.2517-6161.1983.tb01267.x>, Swain et al. (1988)
<doi:10.1080/00949658808811094>, Chen and Shao (1999)
<doi:10.1080/10618600.1999.10474802>, and Balakrishnan and Aggarwala
(2000) <doi:10.1007/978-1-4612-1178-5>.

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
