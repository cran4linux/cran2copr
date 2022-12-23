%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rvif
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collinearity Detection using Redefined Variance Inflation Factor and Graphical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-multiColl 
Requires:         R-CRAN-multiColl 

%description
The detection of troubling approximate collinearity in a multiple linear
regression model is a classical problem in Econometrics. The objective of
this package is to detect it using the variance inflation factor redefined
and the scatterplot between the variance inflation factor and the
coefficient of variation. For more details see Salmerón R., García C.B.
and García J. (2018) <doi:10.1080/00949655.2018.1463376>, Salmerón, R.,
Rodríguez, A. and García C. (2020) <doi:10.1007/s00180-019-00922-x>,
Salmerón, R., García, C.B, Rodríguez, A. and García, C. "Limitations in
Detecting Multicollinearity due to Scaling Issues in the mcvis Package"
(2022, to appear in The R Journal) and Salmerón, R., García, C.B, García
J. (2023, working paper) <arXiv:2005.02245>.

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
