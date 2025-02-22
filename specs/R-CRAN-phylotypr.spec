%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phylotypr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Classifying DNA Sequences to Taxonomic Groupings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-readr >= 2.1.0
BuildRequires:    R-CRAN-Rfast >= 2.1.0
BuildRequires:    R-CRAN-stringi >= 1.8.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-readr >= 2.1.0
Requires:         R-CRAN-Rfast >= 2.1.0
Requires:         R-CRAN-stringi >= 1.8.0
Requires:         R-CRAN-Rcpp 

%description
Classification based analysis of DNA sequences to taxonomic groupings.
This package primarily implements Naive Bayesian Classifier from the
Ribosomal Database Project. This approach has traditionally been used to
classify 16S rRNA gene sequences to bacterial taxonomic outlines; however,
it can be used for any type of gene sequence. The method was originally
described by Wang, Garrity, Tiedje, and Cole in Applied and Environmental
Microbiology 73(16):5261-7 <doi:10.1128/AEM.00062-07>. The package also
provides functions to read in 'FASTA'-formatted sequence data.

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
