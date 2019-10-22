%global packname  timeSeq
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Detecting Differentially Expressed Genes in Time Course RNA-SeqData

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-gss 
BuildRequires:    R-mgcv 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gss 
Requires:         R-mgcv 
Requires:         R-lattice 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-reshape 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
A negative binomial mixed-effects (NBME) model to detect nonparallel
differential expression(NPDE) genes and parallel differential
expression(PDE) genes in the time course RNA-seq data.

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
