%global packname  factorMerger
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}
Summary:          The Merging Path Plot

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-colorRamps 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-agricolae 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-formula.tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-colorRamps 
Requires:         R-CRAN-proxy 
Requires:         R-MASS 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-survival 
Requires:         R-CRAN-agricolae 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-formula.tools 

%description
The Merging Path Plot is a methodology for adaptive fusing of k-groups
with likelihood-based model selection. This package contains tools for
exploration and visualization of k-group dissimilarities. Comparison of
k-groups is one of the most important issues in exploratory analyses and
it has zillions of applications. The traditional approach is to use
pairwise post hoc tests in order to verify which groups differ
significantly. However, this approach fails with a large number of groups
in both interpretation and visualization layer. The Merging Path Plot
solves this problem by using an easy-to-understand description of
dissimilarity among groups based on Likelihood Ratio Test (LRT) statistic
(Sitko, Biecek 2017) <arXiv:1709.04412>. 'factorMerger' is a part of the
'DrWhy.AI' universe (Biecek 2018) <arXiv:1806.08915>. Work on this package
was financially supported by the 'NCN Opus grant 2016/21/B/ST6/02176'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
