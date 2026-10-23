%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SNPAssayR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          SNP Genotyping Assay Design and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Designs cleaved amplified polymorphic sequence (CAPS), derived CAPS
(dCAPS), conventional amplification refractory mutation system (ARMS) and
tetra-primer ARMS assays for single-locus, biallelic single nucleotide
polymorphisms. Evaluates sequence-compatible primer binding, reconstructs
ideal polymerase chain reaction products and computes theoretical complete
restriction digestion and conditional genotype profiles. Transparent
preference ranking, scientific visualizations and reproducible exports
retain assumptions, missing specificity evidence and bounded search
limitations. An optional offline 'shiny' interface uses the independently
available analysis functions. Predictions do not establish experimental
amplification, digestion efficiency or genome-wide specificity. Implements
perfect-match nearest-neighbor thermodynamics from SantaLucia (1998)
<doi:10.1073/pnas.95.4.1460>, single-substitution site-creation dCAPS
based on Neff et al. (1998) <doi:10.1046/j.1365-313X.1998.00124.x>, and
conditional ARMS designs based on Newton et al. (1989)
<doi:10.1093/nar/17.7.2503> and Ye et al. (2001)
<doi:10.1093/nar/29.17.e88>.

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
