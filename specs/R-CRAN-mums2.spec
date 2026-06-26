%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mums2
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Microbial Ecology by Tandem Mass Spectrometry

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-clustur 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mpactr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-RaMS 
BuildRequires:    R-CRAN-sitmo 
BuildRequires:    R-CRAN-RcppThread 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-clustur 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mpactr 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-RaMS 

%description
Tools that researchers can use to analyze untargeted metabolomics data
generated using tandem mass spectroscopy from microbial communities. The
overall approach taken to analyze metabolomics data parallels that used to
analyze microbial communities using 16S rRNA gene sequencing data. Thus,
we have a number of methods a user is able to use to generate data.
Firstly, users can import Mass Spectrometry 1(MS1) data and filter it.
Users are then able to match Mass Spectrometry 2(MS2) data to the filtered
(or unfiltered) MS1 data. With the matched data users are able to cluster
it, annotate it, predict de novo chemical formulas and calculate alpha and
beta diversity. For chemical formula predictions, this was the method
used; "Towards de novo identification of metabolites by analyzing tandem
mass spectra" (Sebastian Böcker, Florian Rasche (2008)
<doi:10.1093/bioinformatics/btn270>). The similarity/dissimilarity
calculations we used to cluster our data together was: "Spectral entropy
outperforms MS/MS dot product similarity for small-molecule compound
identification" (Li, Y., Kind, T., Folz, J. et al. (2021)
<doi:10.1038/s41592-021-01331-z>) and "Sharing and community curation of
mass spectrometry data with Global Natural Products Social Molecular
Networking" (Wang, M., Carver, J., Phelan, V. et al. (2021)
<doi:10.1038/nbt.3597>).

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
