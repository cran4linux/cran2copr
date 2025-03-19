%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TPXG
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two Parameter Xgamma & Poisson Xgamma: Regression & Distribution Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rfast2 
Requires:         R-stats 

%description
The two-parameter Xgamma and Poisson Xgamma distributions are analyzed,
covering standard distribution and regression functions, maximum
likelihood estimation, quantile functions, probability density and mass
functions, cumulative distribution functions, and random number
generation. References include: "Sen, S., Chandra, N. and Maiti, S. S.
(2018). On properties and applications of a two-parameter XGamma
distribution. Journal of Statistical Theory and Applications, 17(4):
674--685. <doi:10.2991/jsta.2018.17.4.9>." "Wani, M. A., Ahmad, P. B.,
Para, B. A. and Elah, N. (2023). A new regression model for count data
with applications to health care data. International Journal of Data
Science and Analytics. <doi:10.1007/s41060-023-00453-1>."

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
