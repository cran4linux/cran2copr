%global packname  SCAT
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Summary Based Conditional Association Test

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Conditional association test based on summary data from genome-wide
association study (GWAS). SCAT adjusts for heterogeneity in SNP coverage
that exists in summary data if SNPs are not present in all of the
participating studies of a GWAS meta-analysis. This commonly happens when
different reference panels are used in participating studies for genotype
imputation. This could happen when ones simply do not have data for some
SNPs (e.g. different array, or imputated data is not available). Without
properly adjusting for this kind of heterogeneity leads to inflated false
positive rate. SCAT can also be used to conduct conventional conditional
analysis when coverage heterogeneity is absent. For more details, refer to
Zhang et al. (2018) Brief Bioinform. 19(6):1337-1343. <doi:
10.1093/bib/bbx072>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
