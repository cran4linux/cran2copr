%global packname  cwbtools
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Tools to create, modify and manage 'CWB' Corpora

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RcppCWB >= 0.2.8
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-methods 
Requires:         R-CRAN-RcppCWB >= 0.2.8
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-pbapply 
Requires:         R-methods 

%description
The 'Corpus Workbench' ('CWB', <http://cwb.sourceforge.net/>) offers a
classic and mature approach for working with large, linguistically and
structurally annotated corpora. The 'CWB' is memory efficient and its
design makes running queries fast (Evert and Hardie 2011,
<http://www.stefan-evert.de/PUB/EvertHardie2011.pdf>). The 'cwbtools'
package offers pure R tools to create indexed corpus files as well as
high-level wrappers for the original C implementation of CWB as exposed by
the 'RcppCWB' package <https://CRAN.R-project.org/package=RcppCWB>.
Additional functionality to add and modify annotations of corpora from
within R makes working with CWB indexed corpora much more flexible and
convenient. The 'cwbtools' package in combination with the R packages
'RcppCWB' (<https://CRAN.R-project.org/package=RcppCWB>) and 'polmineR'
(<https://CRAN.R-project.org/package=polmineR>) offers a lightweight
infrastructure to support the combination of quantitative and qualitative
approaches for working with textual data.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/Rscript
%doc %{rlibdir}/%{packname}/txt
%doc %{rlibdir}/%{packname}/xml
%{rlibdir}/%{packname}/INDEX
