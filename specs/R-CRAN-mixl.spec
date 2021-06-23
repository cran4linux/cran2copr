%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  mixl
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simulated Maximum Likelihood Estimation of Mixed Logit Models for Large Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 

%description
Specification and estimation of multinomial logit models.  Large datasets
and complex models are supported, with an intuitive syntax.  Multinomial
Logit Models, Mixed models, random coefficients and Hybrid Choice are all
supported.  For more information, see Molloy et al. (2019)
<doi:10.3929/ethz-b-000334289>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
