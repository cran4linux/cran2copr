%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metabup
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Analysis Using Basic Uncertain Pooling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-partitions 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-partitions 

%description
Contains functions that allow Bayesian meta-analysis (1) with binomial
data, counts(y) and total counts (n) or, (2) with user-supplied point
estimates and associated variances.  Case (1) provides an analysis based
on the logit transformation of the sample proportion. This methodology is
also appropriate for combining data from sample surveys and related
sources. The functions can calculate the corresponding similarity matrix.
More details can be found in Cahoy and Sedransk (2023), Cahoy and Sedransk
(2022) <doi:10.1007/s42519-018-0027-2>, Evans and Sedransk (2001)
<doi:10.1093/biomet/88.3.643>, and Malec and Sedransk (1992)
<doi:10.1093/biomet/79.3.593>.

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
