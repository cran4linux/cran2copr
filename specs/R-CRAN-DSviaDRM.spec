%global packname  DSviaDRM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Exploring Disease Similarity in Terms of DysfunctionalRegulatory Mechanisms

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-ppcor 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-ppcor 

%description
Elucidation of human disease similarities has emerged as an active
research area, which is highly relevant to etiology, disease
classification, and drug repositioning. This package was designed and
implemented for identifying disease similarities. It contains five
functions which are 'DCEA', 'DCpathway', 'DS', 'comDCGL' and
'comDCGLplot'. In 'DCEA' function, differentially co-expressed genes and
differentially co-expressed links are extracted from disease vs. health
samples. Then 'DCpathway' function assigns differential co-expression
values of pathways to be the average differential co-expression value of
their component genes. Then 'DS' employs partial correlation coefficient
of pathways as the disease similarity for each disease pairs. And 'DS'
contains a permutation process for evaluating the statistical significant
of observed disease partial correlation coefficients. At last, 'comDCGL'
and 'comDCGLplot' sort out shared differentially co-expressed genes and
differentially co-expressed links with regulation information and
visualize them.

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
