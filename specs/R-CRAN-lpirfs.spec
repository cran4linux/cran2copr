%global packname  lpirfs
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Local Projections Impulse Response Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-sandwich >= 2.5.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-plm >= 2.2.3
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-lmtest >= 0.9.36
BuildRequires:    R-CRAN-ggpubr >= 0.3.0
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-sandwich >= 2.5.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-plm >= 2.2.3
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-lmtest >= 0.9.36
Requires:         R-CRAN-ggpubr >= 0.3.0

%description
Provides functions to estimate and plot linear as well as nonlinear
impulse responses based on local projections by Jordà (2005)
<doi:10.1257/0002828053828518>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
