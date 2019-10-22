%global packname  xhmmScripts
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          XHMM R scripts

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-plotrix 

%description
R scripts for plotting and assessing XHMM whole-exome-sequencing-based CNV
calls. XHMM (eXome Hidden Markov Model) is a C++ software package
(http://atgu.mgh.harvard.edu/xhmm) written to call copy number variation
(CNV) from next-generation sequencing projects, where exome capture was
used (or targeted sequencing, more generally). This R package enables the
user to visualize both the PCA normalization performed by XHMM and the
CNVs it has called.

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
