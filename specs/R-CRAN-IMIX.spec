%global packname  IMIX
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Mixture Model for Multi-Omics Data Integration

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-MASS 

%description
A multivariate Gaussian mixture model framework to integrate multiple
types of genomic data and allow modeling of inter-data-type correlations
for association analysis. 'IMIX' can be implemented to test whether a
disease is associated with genes in multiple genomic data types, such as
DNA methylation, copy number variation, gene expression, etc. It can also
study the integration of multiple pathways. 'IMIX' uses the summary
statistics of association test outputs and conduct integration analysis
for two or three types of genomics data. 'IMIX' features
statistically-principled model selection, global FDR control and
computational efficiency. Details are described in Ziqiao Wang and Peng
Wei (2020) <doi:10.1093/bioinformatics/btaa1001>.

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
