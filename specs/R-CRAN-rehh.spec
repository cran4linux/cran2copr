%global packname  rehh
%global packver   3.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          Searching for Footprints of Selection using 'Extended HaplotypeHomozygosity' Based Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rehh.data 
Requires:         R-methods 
Requires:         R-CRAN-rehh.data 

%description
Population genetic data such as 'Single Nucleotide Polymorphisms' (SNPs)
is often used to identify genomic regions that have been under recent
natural or artificial selection and might provide clues about the
molecular mechanisms of adaptation. One approach, the concept of an
'Extended Haplotype Homozygosity' (EHH), introduced by (Sabeti 2002)
<doi:10.1038/nature01140>, has given rise to several statistics designed
for whole genome scans. The package provides functions to compute three of
these, namely: 'iHS' (Voight 2006) <doi:10.1371/journal.pbio.0040072> for
detecting positive or 'Darwinian' selection within a single population as
well as 'Rsb' (Tang 2007) <doi:10.1371/journal.pbio.0050171> and 'XP-EHH'
(Sabeti 2007) <doi:10.1038/nature06250>, targeted at differential
selection between two populations. Various plotting functions are also
included to facilitate visualization and interpretation of these
statistics. Due to changes in the API, albeit mostly minor, versions 3.X
are not compatible with versions 2.0.X. Note: optionally, vcf files can be
imported using package vcfR. That package is currently removed from CRAN,
but can still be installed from <https://github.com/knausb/vcfR> following
instructions there.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
