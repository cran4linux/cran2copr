%global __brp_check_rpaths %{nil}
%global packname  bayMDS
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Multidimensional Scaling and Choice of Dimension

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-progress 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-ggpubr 

%description
Bayesian approach to multidimensional scaling. The package consists of
implementations of the methods of Oh and Raftery (2001)
<doi:10.1198/016214501753208690>.

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
