%global packname  EMpeaksR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conducting the Peak Fitting Based on the EM Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The peak fitting of spectral data is performed by using the frame work of
EM algorithm.  We adapted the EM algorithm for the peak fitting of
spectral data set by considering the weight of the intensity corresponding
to the measurement energy steps (Matsumura, T., Nagamura, N., Akaho, S.,
Nagata, K., & Ando, Y. (2019) <doi:10.1080/14686996.2019.1620123>).  The
package efficiently estimates the parameters of Gaussian mixture model
during iterative calculation between E-step and M-step, and the parameters
are converged to a local optimal solution.  This package can support the
investigation of peak shift with two advantages: (1) a large amount of
data can be processed at high speed; and (2) stable and automatic
calculation can be easily performed.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
