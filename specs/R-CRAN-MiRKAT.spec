%global __brp_check_rpaths %{nil}
%global packname  MiRKAT
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Microbiome Regression-Based Analysis Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-GUniFrac 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-GUniFrac 
Requires:         R-CRAN-PearsonDS 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-survival 
Requires:         R-stats 

%description
Test for overall association between microbiome composition data and
phenotypes via phylogenetic kernels. The phenotype can be univariate
continuous or binary (Zhao et al. (2015)
<doi:10.1016/j.ajhg.2015.04.003>), survival outcomes (Plantinga et al.
(2017) <doi:10.1186/s40168-017-0239-9>), multivariate (Zhan et al. (2017)
<doi:10.1002/gepi.22030>) and structured phenotypes (Zhan et al. (2017)
<doi:10.1111/biom.12684>). The package can also use robust and quantile
regression (unpublished work). In each case, the microbiome community
effect is modeled nonparametrically through a kernel function, which can
incorporate phylogenetic tree information.

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
