%global packname  GAMens
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Applies GAMbag, GAMrsm and GAMens Ensemble Classifiers forBinary Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-caTools 
Requires:         R-splines 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-caTools 

%description
Implements the GAMbag, GAMrsm and GAMens ensemble classifiers for binary
classification (De Bock et al., 2010) <doi:10.1016/j.csda.2009.12.013>.
The ensembles implement Bagging (Breiman, 1996)
<doi:10.1023/A:1010933404324>, the Random Subspace Method (Ho, 1998)
<doi:10.1109/34.709601> , or both, and use Hastie and Tibshirani's (1990,
ISBN:978-0412343902) generalized additive models (GAMs) as base
classifiers. Once an ensemble classifier has been trained, it can be used
for predictions on new data. A function for cross validation is also
included.

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
%{rlibdir}/%{packname}/INDEX
