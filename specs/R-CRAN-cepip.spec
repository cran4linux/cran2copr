%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cepip
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cell Explanatory Power with Inflection Point (CEP-IP) with CMRF

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-parallel 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-openxlsx 

%description
Implements the cell explanatory power with inflection point (CEP-IP)
framework for single-cell co-expression analysis. A generalized additive
model (GAM) fitted by restricted maximum likelihood (REML) with a
penalized residual sum of squares (PRSS) search over the basis dimension
relates a gene of interest to the mean of its partner genes. Cells are
ranked by their explanatory power, and the inflection point is the first
negative-to-positive zero crossing of a residual GAM. Optional extensions
are the Spearman-Kendall cell-level score (SKCS) and the copula monotone
recovery filter (CMRF), which recovers cells near the module through a
tolerance band and a repeated stratified k-fold cross-validation gate.
Downstream helpers give per-donor module fractions, paired donor-level
differential expression and donor-level association models. CEP-IP is
described in Wong (2026) <doi:10.1016/j.cmpb.2026.109372>.

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
