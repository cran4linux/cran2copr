%global packname  pROC
%global packver   1.16.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.16.2
Release:          1%{?dist}
Summary:          Display and Analyze ROC Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14
Requires:         R-core >= 2.14
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-CRAN-plyr 

%description
Tools for visualizing, smoothing and comparing receiver operating
characteristic (ROC curves). (Partial) area under the curve (AUC) can be
compared with statistical tests based on U-statistics or bootstrap.
Confidence intervals can be computed for (p)AUC or ROC curves.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/extra
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
