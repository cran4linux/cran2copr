%global __brp_check_rpaths %{nil}
%global packname  allelematch
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Identifying Unique Multilocus Genotypes where Genotyping Errorand Missing Data may be Present

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dynamicTreeCut 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dynamicTreeCut 

%description
Tools for the identification of unique of multilocus genotypes when both
genotyping error and missing data may be present. The package is targeted
at those working with large datasets and databases containing multiple
samples of each individual, a situation that is common in conservation
genetics, and particularly in non-invasive wildlife sampling applications.
Functions explicitly incorporate missing data, and can tolerate allele
mismatches created by genotyping error. If you use this tool, please cite
the package using the journal article in Molecular Ecology Resources
(Galpern et al., 2012). Please use citation('allelematch') to call the
full citation. For users with access to the associated journal article,
tutorial material is also available as supplementary material to the
article describing this software, the citation for which can be called
using citation('allelematch').

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
