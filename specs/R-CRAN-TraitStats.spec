%global packname  TraitStats
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Data Analysis for Randomized Block Design Experiments

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-rlist 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-qpdf 

%description
Functions for analysis of bulk data generated from experiments in
Randomized block design as per Panse and Sukhatme (1954)
<https://books.google.co.in/books?id=Efo9AAAAYAAJ>. Computes analysis of
variance; Descriptive statistics parameter like Mean, Minimum, Maximum,
CV, Standard error of mean, Standard Error of deviation, CD; Genetic
parameter statistics Genotypic Coefficient of Variation, Phenotypic
Coefficient of Variation, Heritability in broad sense, Genetic Advance and
Genetic Advance per cent mean; Variance and Co-variance matrix of
genotypic, phenotypic and environmental; Correlation of genotypic,
phenotypic and environmental. Further includes directly publication ready
tables.

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
