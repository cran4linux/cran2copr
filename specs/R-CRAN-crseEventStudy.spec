%global __brp_check_rpaths %{nil}
%global packname  crseEventStudy
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Robust and Powerful Test of Abnormal Stock Returns in Long-Horizon Event Studies

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sandwich 

%description
Based on Dutta et al. (2018) <doi:10.1016/j.jempfin.2018.02.004>, this
package provides their standardized test for abnormal returns in
long-horizon event studies. The methods used improve the major weaknesses
of size, power, and robustness of long-run statistical tests described in
Kothari/Warner (2007) <doi:10.1016/B978-0-444-53265-7.50015-9>. Abnormal
returns are weighted by their statistical precision (i.e., standard
deviation), resulting in abnormal standardized returns. This procedure
efficiently captures the heteroskedasticity problem. Clustering techniques
following Cameron et al. (2011) <doi:10.1198/jbes.2010.07136> are adopted
for computing cross-sectional correlation robust standard errors. The
statistical tests in this package therefore accounts for potential biases
arising from returns' cross-sectional correlation, autocorrelation, and
volatility clustering without power loss.

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
