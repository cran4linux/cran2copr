%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phenesse
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Phenological Metrics using Presence-Only Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-stats 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-stats 

%description
Generates Weibull-parameterized estimates of phenology for any percentile
of a distribution using the framework established in Cooke (1979)
<doi:10.1093/biomet/66.2.367>. Extensive testing against other estimators
suggest the weib_percentile() function is especially useful in generating
more accurate and less biased estimates of onset and offset (Belitz et al.
2020) <doi:10.1111/2041-210X.13448>. Non-parametric bootstrapping can be
used to generate confidence intervals around those estimates, although
this is computationally expensive. Additionally, this package offers an
easy way to perform non-parametric bootstrapping to generate confidence
intervals for quantile estimates, mean estimates, or any statistical
function of interest.

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
