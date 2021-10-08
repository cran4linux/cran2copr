%global __brp_check_rpaths %{nil}
%global packname  coga
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Convolution of Gamma Distributions

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-cubature 

%description
Evaluation for density and distribution function of convolution of gamma
distributions in R. Two related exact methods and one approximate method
are implemented with efficient algorithm and C++ code. A quick guide for
choosing correct method and usage of this package is given in package
vignette. For the detail of methods used in this package, we refer the
user to Mathai(1982)<doi:10.1007/BF02481056>,
Moschopoulos(1984)<doi:10.1007/BF02481123>,
Barnabani(2017)<doi:10.1080/03610918.2014.963612>, Hu et
al.(2020)<doi:10.1007/s00180-019-00924-9>.

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
