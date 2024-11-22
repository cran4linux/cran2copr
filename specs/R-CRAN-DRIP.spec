%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DRIP
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Discontinuous Regression and Image Processing

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-stats 

%description
A collection of functions that perform jump regression and image analysis
such as denoising, deblurring and jump detection. The implemented methods
are based on the following research: Qiu, P. (1998)
<doi:10.1214/aos/1024691468>, Qiu, P. and Yandell, B. (1997) <doi:
10.1080/10618600.1997.10474746>, Qiu, P. (2009) <doi:
10.1007/s10463-007-0166-9>, Kang, Y. and Qiu, P. (2014) <doi:
10.1080/00401706.2013.844732>, Qiu, P. and Kang, Y. (2015) <doi:
10.5705/ss.2014.054>, Kang, Y., Mukherjee, P.S. and Qiu, P. (2018) <doi:
10.1080/00401706.2017.1415975>, Kang, Y. (2020) <doi:
10.1080/10618600.2019.1665536>.

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
