%global packname  bPeaks
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          bPeaks: an intuitive peak-calling strategy to detecttranscription factor binding sites from ChIP-seq data in smalleukaryotic genomes

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
bPeaks is a simple approach to identify transcription factor binding sites
from ChIP-seq data. Our general philosophy is to provide an easy-to-use
tool, well-adapted for small eukaryotic genomes (< 20 Mb). bPeaks uses a
combination of 4 cutoffs (T1, T2, T3 and T4) to mimic "good peak"
properties as described by biologists who visually inspect the ChIP-seq
data on a genome browser. For yeast genomes, bPeaks calculates the
proportion of peaks that fall in promoter sequences. These peaks are good
candidates as transcription factor binding sites.

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
