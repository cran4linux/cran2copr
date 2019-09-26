%global packname  seqinr
%global packver   3.6-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.1
Release:          1%{?dist}
Summary:          Biological Sequences Retrieval and Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
Requires:         zlib
BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-segmented 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-segmented 

%description
Exploratory data analysis and data visualization for biological sequence
(DNA and protein) data. Seqinr includes utilities for sequence data
management under the ACNUC system described in Gouy, M. et al. (1984)
Nucleic Acids Res. 12:121-127 <doi:10.1093/nar/12.1Part1.121>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/abif
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/sequences
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
