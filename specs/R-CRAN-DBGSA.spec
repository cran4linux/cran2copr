%global packname  DBGSA
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          methods of distance-based gene set functional enrichmentanalysis.

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.2
Requires:         R-core >= 2.12.2
BuildArch:        noarch
BuildRequires:    R-CRAN-fdrtool >= 1.2.6
Requires:         R-CRAN-fdrtool >= 1.2.6

%description
This package provides methods and examples to support a method of Gene Set
Analysis (GSA).  DBGSA is a novel distance-based gene set enrichment
analysis method. We consider that, the distance between 2 groups with
different phenotype by focusing on the gene expression should be larger,
if a certain gene functional set was significantly associated with a
particular phenotype.

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
