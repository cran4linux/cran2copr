%global packname  earthtide
%global packver   0.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10
Release:          2%{?dist}
Summary:          Parallel Implementation of 'ETERNA 3.40' for Prediction andAnalysis of Earth Tides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.2
BuildRequires:    R-CRAN-R6 >= 2.3.0
BuildRequires:    R-CRAN-BH >= 1.69.0.1
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.200.7.0
Requires:         R-CRAN-RcppParallel >= 4.4.2
Requires:         R-CRAN-R6 >= 2.3.0
Requires:         R-CRAN-Rcpp >= 1.0.0

%description
This is a port of 'Fortran ETERNA 3.4'
<http://igets.u-strasbg.fr/soft_and_tool.php> by H.G. Wenzel for
calculating synthetic Earth tides using the Hartmann and Wenzel (1994)
<doi:10.1029/95GL03324> or Kudryavtsev (2004)
<doi:10.1007/s00190-003-0361-2> tidal catalogs.

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
