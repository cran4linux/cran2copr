%global __brp_check_rpaths %{nil}
%global packname  ampir
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predict Antimicrobial Peptides

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-caret >= 6.0.0
BuildRequires:    R-CRAN-Peptides 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-parallel 
Requires:         R-CRAN-caret >= 6.0.0
Requires:         R-CRAN-Peptides 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-Rcpp 
Requires:         R-parallel 

%description
A toolkit to predict antimicrobial peptides from protein sequences on a
genome-wide scale. It incorporates two support vector machine models
("precursor" and "mature") trained on publicly available antimicrobial
peptide data using calculated physico-chemical and compositional sequence
properties described in Meher et al. (2017) <doi:10.1038/srep42362>. In
order to support genome-wide analyses, these models are designed to accept
any type of protein as input and calculation of compositional properties
has been optimised for high-throughput use. For best results it is
important to select the model that accurately represents your sequence
type: for full length proteins, it is recommended to use the default
"precursor" model. The alternative, "mature", model is best suited for
mature peptide sequences that represent the final antimicrobial peptide
sequence after post-translational processing. For details see Fingerhut et
al. (2020) <doi:10.1093/bioinformatics/btaa653>. The 'ampir' package is
also available via a Shiny based GUI at <https://ampir.marine-omics.net/>.

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
