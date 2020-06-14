%global packname  wdm
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Weighted Dependence Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-Rcpp 

%description
Provides efficient implementations of weighted dependence measures and
related asymptotic tests for independence. Implemented measures are the
Pearson correlation, Spearman's rho, Kendall's tau, Blomqvist's beta, and
Hoeffding's D; see, e.g., Nelsen (2006) <doi:10.1007/0-387-28678-0> and
Hollander et al. (2015, ISBN:9780470387375).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/cmake
%doc %{rlibdir}/%{packname}/CMakeLists.txt
%doc %{rlibdir}/%{packname}/codecov.yml
%{rlibdir}/%{packname}/include
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/test
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
