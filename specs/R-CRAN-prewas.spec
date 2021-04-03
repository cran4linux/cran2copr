%global packname  prewas
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Pre-Processing for Bacterial Genome-Wide Association Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-CRAN-phangorn >= 2.5.5
BuildRequires:    R-CRAN-vcfR >= 1.8.0
BuildRequires:    R-CRAN-future.apply >= 1.3.0
BuildRequires:    R-CRAN-future >= 1.15.1
Requires:         R-CRAN-ape >= 5.3
Requires:         R-stats >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-methods >= 3.5.0
Requires:         R-CRAN-phangorn >= 2.5.5
Requires:         R-CRAN-vcfR >= 1.8.0
Requires:         R-CRAN-future.apply >= 1.3.0
Requires:         R-CRAN-future >= 1.15.1

%description
Standardize the pre-processing of genomic variants before performing a
bacterial genome-wide association study (bGWAS). 'prewas' creates a
variant matrix (where each row is a variant, each column is a sample, and
the entries are presence - 1 - or absence - 0 - of the variant) that can
be used as input for bGWAS tools. When creating the binary variant matrix,
'prewas' can perform 3 pre-processing steps including: dealing with
multiallelic SNPs, (optional) dealing with SNPs in overlapping genes, and
choosing a reference allele. 'prewas' can output matrices for use with
both SNP-based bGWAS and gene-based bGWAS. This method is described in
Saund et al. (2020) <doi:10.1099/mgen.0.000368>. 'prewas' can also provide
gene matrices for variants with specific annotations from the 'SnpEff'
software (Cingolani et al. 2012).

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
