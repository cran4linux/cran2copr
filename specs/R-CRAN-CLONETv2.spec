%global __brp_check_rpaths %{nil}
%global packname  CLONETv2
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Clonality Estimates in Tumor

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-dbscan 
Requires:         R-parallel 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-dbscan 

%description
Analyze data from next-generation sequencing experiments on genomic
samples. 'CLONETv2' offers a set of functions to compute allele specific
copy number and clonality from segmented data and SNPs position pileup.
The package has also calculated the clonality of single nucleotide
variants given read counts at mutated positions. The package has been
developed at the laboratory of Computational and Functional Oncology,
Department of CIBIO, University of Trento (Italy), under the supervision
of prof Francesca Demichelis. References: Prandi et al. (2014)
<doi:10.1186/s13059-014-0439-6>; Carreira et al. (2014)
<doi:10.1126/scitranslmed.3009448>; Romanel et al. (2015)
<doi:10.1126/scitranslmed.aac9511>.

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
