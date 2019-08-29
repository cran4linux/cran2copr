%global packname  HextractoR
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Integrated Tool for Hairping Extraction of RNA Sequences

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-seqinr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Simple and integrated tool that automatically extracts and folds all
hairpin sequences from raw genome-wide data. It predicts the secondary
structure of several overlapped segments, with longer length than the mean
length of sequences of interest for the species under processing, ensuring
that no one is lost nor inappropriately cut.

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
%doc %{rlibdir}/%{packname}/Example_human.fasta
%doc %{rlibdir}/%{packname}/Example_pre-miRNA.fasta
%doc %{rlibdir}/%{packname}/Example_tiny.fasta
%{rlibdir}/%{packname}/INDEX
