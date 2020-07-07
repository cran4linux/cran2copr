%global packname  IROmiss
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Imputation Regularized Optimization Algorithm

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-equSA 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-ncvreg 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-equSA 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-ncvreg 

%description
Missing data are frequently encountered in high-dimensional data analysis,
but they are usually difficult to deal with using standard algorithms,
such as the EM algorithm and its variants. This package provides a general
algorithm, the so-called Imputation Regularized Optimization (IRO)
algorithm, for high-dimensional missing data problems. You can refer to
Liang, F., Jia, B., Xue, J., Li, Q. and Luo, Y. (2018) at
<arXiv:1802.02251> for detail.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
