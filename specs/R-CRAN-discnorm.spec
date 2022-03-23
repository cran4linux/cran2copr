%global __brp_check_rpaths %{nil}
%global packname  discnorm
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Test for Discretized Normality in Ordinal Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.10
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-GoFKernel 
Requires:         R-CRAN-lavaan >= 0.6.10
Requires:         R-CRAN-arules 
Requires:         R-CRAN-sirt 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-GoFKernel 

%description
Tests whether multivariate ordinal data may stem from discretizing a
multivariate normal distribution. The test is described by Foldnes and
Grønneberg (2019) <doi:10.1080/10705511.2019.1673168>. In addition, an
adjusted polychoric correlation estimator is provided that takes marginal
knowledge into account, as described by Grønneberg and Foldnes (2022)
<doi:10.1037/met0000495>.

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
