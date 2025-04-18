%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  skewMLRM
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation for Scale-Shape Mixtures of Skew-Normal Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixcalc 

%description
Provide data generation and estimation tools for the multivariate scale
mixtures of normal presented in Lange and Sinsheimer (1993)
<doi:10.2307/1390698>, the multivariate scale mixtures of skew-normal
presented in Zeller, Lachos and Vilca (2011)
<doi:10.1080/02664760903406504>, the multivariate skew scale mixtures of
normal presented in Louredo, Zeller and Ferreira (2021)
<doi:10.1007/s13571-021-00257-y> and the multivariate scale mixtures of
skew-normal-Cauchy presented in Kahrari et al. (2020)
<doi:10.1080/03610918.2020.1804582>.

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
