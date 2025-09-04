%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MultivariateTrendAnalysis
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Univariate and Multivariate Trend Testing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-resample 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-resample 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-zoo 

%description
With foundations on the work by Goutali and Chebana (2024)
<doi:10.1016/j.envsoft.2024.106090>, this package contains various
univariate and multivariate trend tests. The main functions regard the
Multivariate Dependence Trend and Multivariate Overall Trend tests as
proposed by Goutali and Chebana (2024), as well as a plotting function
that proves useful as a summary and complement of the tests. Although many
packages and methods carry univariate tests, the Mann-Kendall and
Spearman's rho test implementations are included in the package with an
adapted version to hydrological formulation (e.g. as in Rao and Hamed 1998
<doi:10.1016/S0022-1694(97)00125-X> or Chebana 2022
<doi:10.1016/C2021-0-01317-1>). For better understanding of the example
use of the functions, three datasets are included. These are synthetic
data and shouldn't be used beyond that purpose.

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
