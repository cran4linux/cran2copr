%global __brp_check_rpaths %{nil}
%global packname  lime
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Local Interpretable Model-Agnostic Explanations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gower 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-tools 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-gower 

%description
When building complex models, it is often difficult to explain why the
model should be trusted. While global measures such as accuracy are
useful, they cannot be used for explaining why a model made a specific
prediction. 'lime' (a port of the 'lime' 'Python' package) is a method for
explaining the outcome of black box models by fitting a local model around
the point in question an perturbations of this point. The approach is
described in more detail in the article by Ribeiro et al. (2016)
<arXiv:1602.04938>.

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
