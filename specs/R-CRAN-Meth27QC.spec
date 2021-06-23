%global __brp_check_rpaths %{nil}
%global packname  Meth27QC
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Meth27QC: sample quality analysis, and sample control analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-tcltk 
Requires:         R-CRAN-gplots 
Requires:         R-tcltk 

%description
Meth27QC is a tool for analyzing Illumina Infinium HumanMethylation27
BeadChip Data and generating QC reports. This package allows users quickly
assess data quality of the Assay. Users can evaluate the data quality in
the way that Illumina GenomeStudio/BeadStudio recommended based on the
control probes. The package reads files exported from
GenomeStudio/BeadStudio software, generating intensity and standard
deviation plots grouped by the types of the control probes. Meth27 carries
40 control probes for staining, hybridization, target removal, extension,
bisulfite conversion, specificity, negative and non-polymorphic controls.
Details of those control probes can be found in the Infinium Assay for
Methylation Protocol Guide from Illumina.We also used the other
non-control probes to plot intensity of detected genes, signal average for
green and red. Outliers can be identified.

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
%{rlibdir}/%{packname}/datafile
%doc %{rlibdir}/%{packname}/DemoData
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
