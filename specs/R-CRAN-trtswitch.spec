%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trtswitch
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Treatment Switching

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-cowplot >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-cowplot >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.10
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.6

%description
Implements rank preserving structural failure time model (RPSFTM),
iterative parameter estimation (IPE), inverse probability of censoring
weights (IPCW), marginal structural model (MSM), simple two-stage
estimation (TSEsimp), and improved two-stage estimation with g-estimation
(TSEgest) methods for treatment switching in randomized clinical trials.

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
