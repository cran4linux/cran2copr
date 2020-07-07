%global packname  CREAM
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Clustering of Genomic Regions Analysis Method

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a new method for identification of clusters of genomic regions
within chromosomes. Primarily, it is used for calling clusters of
cis-regulatory elements (COREs). 'CREAM' uses genome-wide maps of genomic
regions in the tissue or cell type of interest, such as those generated
from chromatin-based assays including DNaseI, ATAC or ChIP-Seq. 'CREAM'
considers proximity of the elements within chromosomes of a given sample
to identify COREs in the following steps: 1) It identifies window size or
the maximum allowed distance between the elements within each CORE, 2) It
identifies number of elements which should be clustered as a CORE, 3) It
calls COREs, 4) It filters the COREs with lowest order which does not pass
the threshold considered in the approach.

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
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
