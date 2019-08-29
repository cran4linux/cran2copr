%global packname  Biopeak
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Identification of Impulse-Like Gene Expression Changes in ShortGenomic Series Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-graphics 

%description
Enables the user to systematically identify and visualize impulse-like
gene expression changes within short genomic series experiments. In order
to detect such activation peaks, the gene expression is treated as a
signal that propagates along an experimental axis (time, temperature or
other series conditions). Peaks are selected by exhaustive identification
of local maximums and subsequent filtering based on a range of
controllable parameters. Moreover, the 'Biopeak' package provides a series
of data exploration tools including: expression profile plots, correlation
heat maps and clustering functionalities.

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
%{rlibdir}/%{packname}/INDEX
