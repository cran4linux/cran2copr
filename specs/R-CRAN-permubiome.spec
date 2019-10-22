%global packname  permubiome
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          A Permutation Based Test for Biomarker Discovery in MicrobiomeData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

%description
The permubiome R package was created to perform a permutation-based
non-parametric analysis on microbiome data for biomarker discovery aims.
This test executes thousands of comparisons in a pairwise manner, after a
random shuffling of data into the different groups of study with prior
selection of the microbiome features with the largest variation among
groups. Previous to the permutation test itself, data can be normalized
according to different methods proposed to handle microbiome data
('proportions', 'anders', and 'paulson'). The median-based differences
between groups resulting from the multiple simulations are fitted to a
normal distribution with the aim to calculate their significance. A
multiple testing correction based on Benjamini-Hochberg method (fdr) is
finally applied to extract the differentially presented features between
groups of your dataset. LATEST UPDATES: v1.1 and olders incorporates
function to parse BIOM-like format; v1.2 and olders incorporates
"optimize" function to maximize evaluation of features with largest
inter-class variation.

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
%doc %{rlibdir}/%{packname}/extdat
%{rlibdir}/%{packname}/INDEX
