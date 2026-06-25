%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  moderncor
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified Interface for Modern and Classical Correlation Coefficients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-XICOR 
Requires:         R-stats 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-XICOR 

%description
Provides a single unified interface for computing a wide variety of
classical and modern correlation and association measures. Continuous
methods include classical correlations (Pearson, Spearman, Kendall),
modern dependence measures (distance correlation, maximal information
coefficient, Hilbert-Schmidt independence criterion, Chatterjee's xi,
Hoeffding's D, mutual information), robust correlations (biweight
midcorrelation, percentage bend, Winsorized), ordinal correlations
(polychoric, tetrachoric), partial and semi-partial correlations, and
nonparametric measures (ball correlation, Bergsma-Dassios tau*).
Categorical association measures (Cramer's V, phi coefficient,
Goodman-Kruskal gamma, Somers' D, contingency coefficient, Tschuprow's T)
are available via moderncor_cat().

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
