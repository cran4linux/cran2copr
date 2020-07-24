%global packname  tcftt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Two-Sample Tests for Skewed Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The classical two-sample t-test works well for the normally distributed
data or data with large sample size. The tcfu() and tt() tests implemented
in this package provide better type-I-error control with more accurate
power when testing the equality of two-sample means for skewed populations
having unequal variances. These tests are especially useful when the
sample sizes are moderate. The tcfu() uses the Cornish-Fisher expansion to
achieve a better approximation to the true percentiles. The tt() provides
transformations of the Welch's t-statistic so that the sampling
distribution become more symmetric. For more technical details, please
refer to Zhang (2019) <http://hdl.handle.net/2097/40235>.

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
