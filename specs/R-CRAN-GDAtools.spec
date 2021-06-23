%global __brp_check_rpaths %{nil}
%global packname  GDAtools
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolbox for Geometric Data Analysis and More

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-wdm 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-GGally 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-wdm 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-GGally 

%description
Contains functions for 'specific' Multiple Correspondence Analysis, Class
Specific Analysis, Multiple Factor Analysis, 'standardized' MCA, computing
and plotting structuring factors and concentration ellipses, inductive
tests and others tools for Geometric Data Analysis (Le Roux & Rouanet
(2005) <doi:10.1007/1-4020-2236-0>). It also provides functions for the
translation of logit models coefficients into percentages (Deauvieau
(2010) <doi:10.1177/0759106309352586>), weighted contingency tables, an
association measure for contingency tables ("Percentages of Maximum
Deviation from Independence", aka PEM, see Cibois (1993)
<doi:10.1177/075910639304000103>) and some tools to measure and plot
bivariate associations between variables (phi, Cramér V, correlation
coefficient, eta-squared...).

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
