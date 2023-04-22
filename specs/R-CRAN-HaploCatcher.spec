%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HaploCatcher
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          A Predictive Haplotyping Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-base 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-randomForest 

%description
Used for predicting a genotype’s allelic state at a specific
locus/QTL/gene. This is accomplished by using both a genotype matrix and a
separate file which has categorizations about loci/QTL/genes of interest
for the individuals in the genotypic matrix. A training population can be
created from a panel of individuals who have been previously screened for
specific loci/QTL/genes, and this previous screening could be summarized
into a category. Using the categorization of individuals which have been
genotyped using a genome wide marker platform, a model can be trained to
predict what category (haplotype) an individual belongs in based on their
genetic sequence in the region associated with the locus/QTL/gene. These
trained models can then be used to predict the haplotype of a
locus/QTL/gene for individuals which have been genotyped with a genome
wide platform yet not genotyped for the specific locus/QTL/gene. This
package is based off work done by Winn et al 2021. For more specific
information on this method, refer to <doi:10.1007/s00122-022-04178-w>.

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
