%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MixtureMissing
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Model-Based Clustering for Data Sets with Missing Values at Random

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 8.1.1
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-cluster >= 2.1.2
BuildRequires:    R-CRAN-mnormt >= 2.0.2
BuildRequires:    R-CRAN-mvtnorm >= 1.1.2
BuildRequires:    R-CRAN-Bessel >= 0.6.0
Requires:         R-CRAN-numDeriv >= 8.1.1
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-cluster >= 2.1.2
Requires:         R-CRAN-mnormt >= 2.0.2
Requires:         R-CRAN-mvtnorm >= 1.1.2
Requires:         R-CRAN-Bessel >= 0.6.0

%description
Implementation of robust model-based cluster analysis for data sets with
missing values at random. The models used are: Multivariate Contaminated
Normal Mixture (MCNM, Tong and Tortora, 2022,
<doi:10.1007/s11634-021-00476-1>), Multivariate Generalized Hyperbolic
Mixture (MGHM, Wei et al., 2019, <doi:10.1016/j.csda.2018.08.016>),
Multivariate Skew's t Mixture (MStM, Wei et al., 2019,
<doi:10.1016/j.csda.2018.08.016>), Multivariate t Mixture (MtM, Wang et
al., 2004, <doi:10.1016/j.patrec.2004.01.010>), and Multivariate Normal
Mixture (MNM, Ghahramani and Jordan, 1994, <doi:10.21236/ADA295618>).

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
