%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SNPfiltR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Interactively Filter SNP Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggridges 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Is designed to interactively and reproducibly visualize and filter SNP
(single-nucleotide polymorphism) datasets. This R-based implementation of
SNP and genotype filters facilitates an interactive and iterative SNP
filtering pipeline, which can be documented reproducibly via Rmarkdown.
'SNPfiltR' contains functions for visualizing various quality and missing
data metrics for a SNP dataset, and then filtering the dataset based on
user specified cutoffs. All functions take 'vcfR' objects as input, which
can easily be generated by reading standard vcf (variant call format)
files into R using the R package 'vcfR' (Knaus and Grünwald)
(<doi:10.1111/1755-0998.12549>). Each 'SNPfiltR' function can return a
newly filtered vcfR object, which can then be written to a local directory
in standard vcf format using the 'vcfR' package, for downstream population
genetic and phylogenetic analyses.

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
