%global packname  CalibrateSSB
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Weighting and Estimation for Panel Data with Non-Response

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-methods 
Requires:         R-CRAN-survey 
Requires:         R-methods 

%description
Functions to calculate weights, estimates of changes and corresponding
variance estimates for panel data with non-response. Partially overlapping
samples are handled. Initially, weights are calculated by linear
calibration. By default, the survey package is used for this purpose. It
is also possible to use ReGenesees, which can be installed from
<https://github.com/DiegoZardetto/ReGenesees>. Variances of linear
combinations (changes and averages) and ratios are calculated from a
covariance matrix based on residuals according to the calibration model.
The methodology was presented at the conference, The Use of R in Official
Statistics, and is described in Langsrud (2016)
<http://www.revistadestatistica.ro/wp-content/uploads/2016/06/RRS2_2016_A021.pdf>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
