%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RSStest
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Testing the Equality of Two Means Using RSS and MRSS

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-huxtable >= 5.4.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-huxtable >= 5.4.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Testing the equality of two means using Ranked Set Sampling and Median
Ranked Set Sampling are provided under normal distribution. Data
generation functions are also given RSS and MRSS. Also, data generation
functions are given under imperfect ranking data for Ranked Set Sampling
and Median Ranked Set Sampling. Ozdemir Y.A., Ebegil M., & Gokpinar F.
(2019), <doi:10.1007/s40995-018-0558-0> Ozdemir Y.A., Ebegil M., &
Gokpinar F. (2017), <doi:10.1080/03610918.2016.1263736>.

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
