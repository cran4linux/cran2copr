%global packname  gtWAS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Genome and Transcriptome Wide Association Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Quantitative trait loci mapping and genome wide association analysis are
used to find candidate molecular marker or region associated with
phenotype based on linkage analysis and linkage disequilibrium. Gene
expression quantitative trait loci mapping is used to find candidate
molecular marker or region associated with gene expression. In this
package, we applied the method in Liu W. (2011)
<doi:10.1007/s00122-011-1631-7> and Gusev A. (2016) <doi:10.1038/ng.3506>
to genome and transcriptome wide association study, which is aimed at
revealing the association relationship between phenotype and molecular
markers, expression levels, molecular markers nested within different
related expression effect and expression effect nested within different
related molecular marker effect. F test based on full and reduced model
are performed to obtain p value or likelihood ratio statistic. The best
linear model can be obtained by stepwise regression analysis.

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
