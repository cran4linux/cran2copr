%global packname  HAPim
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          HapIM

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The package provides a set of functions whose aim is to propose 4 methods
of QTL detection. HAPimLD is an interval-mapping method designed for
unrelated individuals with no family information that makes use of linkage
disequilibrium. HAPimLDL is an interval-mapping method for design of
half-sib families. It combines linkage analysis and linkage
disequilibrium. HaploMax is based on an analysis of variance with a dose
haplotype effect. HaploMaxHS is based on an analysis of variance with a
sire effect and a dose haplotype effect in half-sib family design.
Fundings for the package development were provided to the LDLmapQTL
project by the ANR GENANIMAL program and APIS-GENE.

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
%{rlibdir}/%{packname}/INDEX
