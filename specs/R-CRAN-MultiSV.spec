%global packname  MultiSV
%global packver   0.0-67
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.67
Release:          1%{?dist}
Summary:          MultiSV: an R package for identification of structuralvariations in multiple populations based on whole genomeresequencing

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-reshape 
Requires:         R-nlme 
Requires:         R-CRAN-reshape 

%description
MultiSV is an R package for identification of structural variations in
multiple populations based on whole genome resequencing. It fits linear
mixed model and identifies structural variations in multiple populations
using whole genome sequencing data. It could also be manipulated to use on
RNA-seq data for differential gene expression (implementation in future
releases). Main steps for analysis include generating read depth in bins
using ComputeBinCounts. conversion of bins to MultiSV format using
Bin2MultiSV. Finally, identification of structural variations using
CallMultiSV.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/RPRL
%{rlibdir}/%{packname}/INDEX
