%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bfpwr
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Power and Sample Size Calculations for Bayes Factor Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lamW 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-qrng 
BuildRequires:    R-utils 
Requires:         R-CRAN-lamW 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-qrng 
Requires:         R-utils 

%description
Implements z-test, t-test, normal moment prior, and binomial test Bayes
factors based on summary statistics, along with functionality to perform
corresponding power and sample size calculations for fixed and sequential
designs as described in Pawel and Held (2025)
<doi:10.1080/00031305.2025.2467919>, Pawel and Held (2026)
<doi:10.48550/ARXIV.2601.02851>, and Kelter and Pawel (2026)
<doi:10.48550/arXiv.2502.02914>.

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
