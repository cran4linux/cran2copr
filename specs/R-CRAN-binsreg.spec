%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binsreg
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Binscatter Estimation and Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-CRAN-matrixStats 

%description
Provides tools for statistical analysis using the binscatter methods
developed by Cattaneo, Crump, Farrell and Feng (2024a)
<doi:10.48550/arXiv.1902.09608>, Cattaneo, Crump, Farrell and Feng (2024b)
<https://nppackages.github.io/references/Cattaneo-Crump-Farrell-Feng_2024_NonlinearBinscatter.pdf>
and Cattaneo, Crump, Farrell and Feng (2024c)
<doi:10.48550/arXiv.1902.09615>. Binscatter provides a flexible way of
describing the relationship between two variables based on
partitioning/binning of the independent variable of interest. binsreg(),
binsqreg() and binsglm() implement binscatter least squares regression,
quantile regression and generalized linear regression respectively, with
particular focus on constructing binned scatter plots. They also implement
robust (pointwise and uniform) inference of regression functions and
derivatives thereof. binstest() implements hypothesis testing procedures
for parametric functional forms of and nonparametric shape restrictions on
the regression function. binspwc() implements hypothesis testing
procedures for pairwise group comparison of binscatter estimators.
binsregselect() implements data-driven procedures for selecting the number
of bins for binscatter estimation. All the commands allow for covariate
adjustment, smoothness restrictions and clustering.

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
