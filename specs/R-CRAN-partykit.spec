%global packname  partykit
%global packver   1.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          A Toolkit for Recursive Partytioning

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-rpart >= 4.1.11
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-libcoin >= 1.0.0
BuildRequires:    R-CRAN-inum >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-survival 
Requires:         R-rpart >= 4.1.11
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-libcoin >= 1.0.0
Requires:         R-CRAN-inum >= 1.0.0
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-mvtnorm 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-survival 

%description
A toolkit with infrastructure for representing, summarizing, and
visualizing tree-structured regression and classification models. This
unified infrastructure can be used for reading/coercing tree models from
different sources ('rpart', 'RWeka', 'PMML') yielding objects that share
functionality for print()/plot()/predict() methods. Furthermore, new and
improved reimplementations of conditional inference trees (ctree()) and
model-based recursive partitioning (mob()) from the 'party' package are
provided based on the new infrastructure. A description of this package
was published by Hothorn and Zeileis (2015)
<http://jmlr.org/papers/v16/hothorn15a.html>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/pmml
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
