%global __brp_check_rpaths %{nil}
%global packname  PAsso
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Assessing the Partial Association Between Ordinal Variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS >= 7.3.51.0
BuildRequires:    R-utils >= 3.5.3
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-pcaPP >= 1.9.73
BuildRequires:    R-CRAN-foreach >= 1.4.8
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-copBasic 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MASS >= 7.3.51.0
Requires:         R-utils >= 3.5.3
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-pcaPP >= 1.9.73
Requires:         R-CRAN-foreach >= 1.4.8
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-copBasic 
Requires:         R-methods 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-copula 

%description
An implementation of the unified framework for assessing partial
association between ordinal variables after adjusting for a set of
covariates (Dungang Liu, Shaobo Li, Yan Yu and Irini Moustaki (2020),
accepted by the Journal of the American Statistical Association). This
package provides a set of tools to quantify, visualize, and test partial
associations between multiple ordinal variables. It can produce a number
of $phi$ measures, partial regression plots, 3-D plots, and $p$-values for
testing $H_0: phi=0$ or $H_0: phi <= delta$.

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
