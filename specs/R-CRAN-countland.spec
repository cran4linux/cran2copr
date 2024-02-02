%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countland
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Biological Count Data, Especially from Single-Cell RNA-Seq

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 

%description
A set of functions for applying a restricted linear algebra to the
analysis of count-based data. See the accompanying preprint manuscript:
"Normalizing need not be the norm: count-based math for analyzing
single-cell data" Church et al (2022) <doi:10.1101/2022.06.01.494334> This
tool is specifically designed to analyze count matrices from single cell
RNA sequencing assays. The tools implement several count-based approaches
for standard steps in single-cell RNA-seq analysis, including scoring
genes and cells, comparing cells and clustering, calculating differential
gene expression, and several methods for rank reduction. There are many
opportunities for further optimization that may prove useful in the
analysis of other data. We provide the source code freely available at
<https://github.com/shchurch/countland> and encourage users and developers
to fork the code for their own purposes.

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
