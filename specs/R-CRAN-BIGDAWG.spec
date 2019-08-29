%global packname  BIGDAWG
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Case-Control Analysis of Multi-Allelic Loci

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-haplo.stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-haplo.stats 
Requires:         R-parallel 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 

%description
Data sets and functions for chi-squared Hardy-Weinberg and case-control
association tests of highly polymorphic genetic data [e.g., human
leukocyte antigen (HLA) data]. Performs association tests at multiple
levels of polymorphism (haplotype, locus and HLA amino-acids) as described
in Pappas DJ, Marin W, Hollenbach JA, Mack SJ (2016)
<doi:10.1016/j.humimm.2015.12.006>. Combines rare variants to a common
class to account for sparse cells in tables as described by Hollenbach JA,
Mack SJ, Thomson G, Gourraud PA (2012) <doi:10.1007/978-1-61779-842-9_14>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
