%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R2Addhaz
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R2 Measure of Explained Variation under the Additive Hazards Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-ahaz 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-ahaz 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-survival 

%description
R^2 measure of explained variation under the semiparametric additive
hazards model is estimated. The measure can be used as a measure of
predictive capability and therefore it can be adopted in model selection
process. Rava, D. and Xu, R. (2020) <arXiv:2003.09460>.

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
