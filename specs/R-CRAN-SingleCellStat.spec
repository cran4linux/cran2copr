%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SingleCellStat
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Statistical Analysis of Single-Cell Omics Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-vegan 

%description
A suite of statistical methods for analysis of single-cell omics data
including linear model-based methods for differential abundance analysis
for individual level single-cell RNA-seq data. For more details see Zhang,
et al. (Submitted to
Bioinformatics)<https://github.com/Lujun995/DiSC_Replication_Code>.

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
