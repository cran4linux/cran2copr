%global __brp_check_rpaths %{nil}
%global packname  sumFREGAT
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Region-Based Association Tests on Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-seqminer 
BuildRequires:    R-CRAN-GBJ 
Requires:         R-methods 
Requires:         R-CRAN-Matrix 
Requires:         R-splines 
Requires:         R-CRAN-seqminer 
Requires:         R-CRAN-GBJ 

%description
An adaptation of classical region/gene-based association analysis
techniques to the use of summary statistics (P values and effect sizes)
and correlations between genetic variants as input. It is a tool to
perform the most popular and efficient gene-based tests using the results
of genome-wide association (meta-)analyses without having the original
genotypes and phenotypes at hand. See for details: Svishcheva et al (2019)
Gene-based association tests using GWAS summary statistics.
Bioinformatics. Belonogova et al (2022) SumSTAAR: A flexible framework for
gene-based association studies using GWAS summary statistics. PLOS Comp
Biol.

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
