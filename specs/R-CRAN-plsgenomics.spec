%global __brp_check_rpaths %{nil}
%global packname  plsgenomics
%global packver   1.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          PLS Analyses for Genomics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RhpcBLASctl 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-RhpcBLASctl 

%description
Routines for PLS-based genomic analyses, implementing PLS methods for
classification with microarray data and prediction of transcription factor
activities from combined ChIP-chip analysis. The >=1.2-1 versions include
two new classification methods for microarray data: GSIM and Ridge PLS.
The >=1.3 versions includes a new classification method combining variable
selection and compression in logistic regression context: logit-SPLS; and
an adaptive version of the sparse PLS.

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
