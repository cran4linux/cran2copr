%global packname  interflex
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Multiplicative Interaction Models Diagnostics and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-lfe >= 2.6.2291
BuildRequires:    R-CRAN-sandwich >= 2.3.4
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-pcse >= 1.9
BuildRequires:    R-mgcv >= 1.8.16
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-Lmoments >= 1.2.3
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-lmtest >= 0.9.34
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-lfe >= 2.6.2291
Requires:         R-CRAN-sandwich >= 2.3.4
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-pcse >= 1.9
Requires:         R-mgcv >= 1.8.16
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-Lmoments >= 1.2.3
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-lmtest >= 0.9.34
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-gtable 

%description
Performs diagnostic tests of multiplicative interaction models and plots
non-linear marginal effects of a treatment on an outcome across different
values of a moderator.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
