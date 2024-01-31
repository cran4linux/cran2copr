%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ardl.nardl
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Linear and Nonlinear Autoregressive Distributed Lag Models: General-to-Specific Approach

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gets 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-nardl 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-gets 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-nardl 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyselect 

%description
Estimate the linear and nonlinear autoregressive distributed lag (ARDL &
NARDL) models and the corresponding error correction models, and test for
longrun and short-run asymmetric. The general-to-specific approach is also
available in estimating the ARDL and NARDL models. The Pesaran, Shin &
Smith (2001) (<doi:10.1002/jae.616>) bounds test for level relationships
is also provided. The 'ardl.nardl' package also performs short-run and
longrun symmetric restrictions available at Shin et al. (2014)
<doi:10.1007/978-1-4899-8008-3_9> and their corresponding tests.

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
