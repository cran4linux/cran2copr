%global packname  PAGI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          The package can identify the dysregulated KEGG pathways based onglobal influence from the internal effect of pathways andcrosstalk between pathways.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
The package can identify the dysregulated KEGG pathways based on global
influence from the internal effect of pathways and crosstalk between
pathways. (1) The PAGI package can prioritize the pathways associated with
two biological states by statistical significance or FDR. (2) The PAGI
package can evaluated the global influence factor (GIF) score in the
global gene-gene network constructed based on the relationships of genes
extracted from each pathway in KEGG database and the overlapped genes
between pathways.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/localdata
%{rlibdir}/%{packname}/INDEX
