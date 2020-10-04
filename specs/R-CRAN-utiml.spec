%global packname  utiml
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Utilities for Multi-Label Learning

License:          GPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mldr >= 0.4.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-mldr >= 0.4.0
Requires:         R-parallel 
Requires:         R-CRAN-ROCR 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Multi-label learning strategies and others procedures to support multi-
label classification in R. The package provides a set of multi-label
procedures such as sampling methods, transformation strategies, threshold
functions, pre-processing techniques and evaluation metrics. A complete
overview of the matter can be seen in Zhang, M. and Zhou, Z. (2014)
<doi:10.1109/TKDE.2013.39> and Gibaja, E. and Ventura, S. (2015) A
Tutorial on Multi-label Learning.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
