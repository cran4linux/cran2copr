%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EMGCR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fit a Mixture Cure Rate Model with Custom Link Function

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 

%description
Tools to fit Mixture Cure Rate models via the Expectation-Maximization
(EM) algorithm, allowing for flexible link functions in the cure component
and various survival distributions in the latency part. The package
supports user-specified link functions, includes methods for parameter
estimation and model diagnostics, and provides residual analysis tailored
for cure models. The classical theory methods used are described in
Berkson, J. and Gage, R. P. (1952) <doi:10.2307/2281318>, Dempster, A. P.,
Laird, N. M. and Rubin, D. B. (1977)
<https://www.jstor.org/stable/2984875>, Bazán, J., Torres-Avilés, F.,
Suzuki, A. and Louzada, F. (2017)<doi:10.1002/asmb.2215>.

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
