%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hdcce
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Inference for High-Dimensional Panel Data Models with Interactive Fixed Effects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mvtnorm 

%description
Estimation and inference for panel data models with interactive fixed
effects. The methods cover i) the linear specification of Ruecker, M.,
Vogt, M., Linton, O. and Walsh, C. (2025) "Estimation and Inference in
High-Dimensional Panel Data Models with Interactive Fixed Effects"
<doi:10.3982/QE2308>, and ii) the dictionary design of Ruecker, M., Vogt,
M. and Linton, O. (2026) "High-Dimensional Panel Data Models with
Interactive Fixed Effects: Beyond the Linear Case"
<doi:10.48550/arXiv.2608.02055>.

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
