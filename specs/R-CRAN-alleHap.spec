%global __brp_check_rpaths %{nil}
%global packname  alleHap
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          3%{?dist}%{?buildtag}
Summary:          Allele Imputation and Haplotype Reconstruction from PedigreeDatabases

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-abind 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to simulate alphanumeric alleles, impute genetic missing data and
reconstruct non-recombinant haplotypes from pedigree databases in a
deterministic way. Allelic simulations can be implemented taking into
account many factors (such as number of families, markers, alleles per
marker, probability and proportion of missing genotypes, recombination
rate, etc). Genotype imputation can be used with simulated datasets or
real databases (previously loaded in .ped format). Haplotype
reconstruction can be carried out even with missing data, since the
program firstly imputes each family genotype (without a reference panel),
to later reconstruct the corresponding haplotypes for each family member.
All this considering that each individual (due to meiosis) should
unequivocally have two alleles per marker (one inherited from each parent)
and thus imputation and reconstruction results can be deterministically
calculated.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX
