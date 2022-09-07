%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IRTest
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter Estimation of Item Response Theory with Estimation of Latent Distribution

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-betafunctions 
BuildRequires:    R-CRAN-dcurver 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-betafunctions 
Requires:         R-CRAN-dcurver 
Requires:         R-CRAN-ggplot2 

%description
Item response theory (IRT) parameter estimation using marginal maximum
likelihood and expectation-maximization algorithm (Bock & Aitkin, 1981
<doi:10.1007/BF02293801>). Within parameter estimation algorithm, several
methods for latent distribution estimation are available (Li, 2022
<https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=9a95f68e2c1126c5ffe0bdc3ef48d419>).
Reflecting some features of the true latent distribution, these latent
distribution estimation methods can possibly free the normality assumption
on the latent distribution.

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
