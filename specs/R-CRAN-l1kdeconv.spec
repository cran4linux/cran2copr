%global packname  l1kdeconv
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          2%{?dist}
Summary:          Deconvolution for LINCS L1000 Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mixtools 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-mixtools 
Requires:         R-CRAN-ggplot2 

%description
LINCS L1000 is a high-throughput technology that allows the gene
expression measurement in a large number of assays. However, to fit the
measurements of ~1000 genes in the ~500 color channels of LINCS L1000,
every two landmark genes are designed to share a single channel. Thus, a
deconvolution step is required to infer the expression values of each
gene. Any errors in this step can be propagated adversely to the
downstream analyses. We present a LINCS L1000 data peak calling R package
l1kdeconv based on a new outlier detection method and an aggregate
Gaussian mixture model. Upon the remove of outliers and the borrowing
information among similar samples, l1kdeconv shows more stable and better
performance than methods commonly used in LINCS L1000 data deconvolution.

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
%{rlibdir}/%{packname}/INDEX
