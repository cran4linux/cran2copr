%global packname  dcminfo
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Information Matrix for Diagnostic Classification Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-CDM 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 

%description
A set of asymptotic methods that can be used to directly estimate the
expected (Fisher) information matrix by Liu, Tian, and Xin (2016)
<doi:10.3102/1076998615621293> in diagnostic classification models or
cognitive diagnostic models are provided when marginal maximum likelihood
estimation is used. For these methods, both the item and structural model
parameters are considered simultaneously. Specifically, the observed
information matrix, the empirical cross-product information matrix and the
sandwich-type co-variance matrix that can be used to estimate the
asymptotic co-variance matrix (or the model parameter standard errors)
within the context of diagnostic classification models are provided.

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
%{rlibdir}/%{packname}/INDEX
