%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  extrafrail
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Additional Tools for Alternative Shared Frailty Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-msm 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-msm 

%description
Provide estimation and data generation tools for some new multivariate
frailty models. This version includes the gamma, inverse Gaussian,
weighted Lindley, Birnbaum-Saunders, truncated normal and mixture of
inverse Gaussian as the distribution for the frailty terms. For the basal
model, it is considered a parametric approach based on the exponential,
Weibull and the piecewise exponential distributions as well as a
semiparametric approach. For details, see Gallardo and Bourguignon (2022)
<arXiv:2206.12973>.

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
