%global packname  AntAngioCOOL
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Anti-Angiogenic Peptide Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-rpart 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-RWeka 
Requires:         R-rpart 

%description
Machine learning based package to predict anti-angiogenic peptides using
heterogeneous sequence descriptors. 'AntAngioCOOL' exploits five
descriptor types of a peptide of interest to do prediction including:
pseudo amino acid composition, k-mer composition, k-mer composition
(reduced alphabet), physico-chemical profile and atomic profile. According
to the obtained results, 'AntAngioCOOL' reached to a satisfactory
performance in anti-angiogenic peptide prediction on a benchmark
non-redundant independent test dataset.

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
