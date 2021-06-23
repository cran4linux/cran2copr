%global __brp_check_rpaths %{nil}
%global packname  plinkQC
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Genotype Quality Control with 'PLINK'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-data.table >= 1.11.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-UpSetR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-sys 
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-data.table >= 1.11.0
Requires:         R-methods 
Requires:         R-CRAN-optparse 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-UpSetR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-sys 

%description
Genotyping arrays enable the direct measurement of an individuals genotype
at thousands of markers. 'plinkQC' facilitates genotype quality control
for genetic association studies as described by Anderson and colleagues
(2010) <doi:10.1038/nprot.2010.116>. It makes 'PLINK' basic statistics
(e.g. missing genotyping rates per individual, allele frequencies per
genetic marker) and relationship functions accessible from 'R' and
generates a per-individual and per-marker quality control report.
Individuals and markers that fail the quality control can subsequently be
removed to generate a new, clean dataset. Removal of individuals based on
relationship status is optimised to retain as many individuals as possible
in the study.

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
