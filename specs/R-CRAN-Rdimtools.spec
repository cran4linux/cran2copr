%global packname  Rdimtools
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Dimension Reduction and Estimation Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-CVXR >= 0.95
BuildRequires:    R-CRAN-ADMM >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-Rcsdp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-Matrix 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppDE 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CVXR >= 0.95
Requires:         R-CRAN-ADMM >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-Rcsdp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSpectra 
Requires:         R-Matrix 
Requires:         R-utils 
Requires:         R-CRAN-RcppDE 

%description
We provide linear and nonlinear dimension reduction techniques. Intrinsic
dimension estimation methods for exploratory analysis are also provided.
For more details on dimensionality techniques, see the paper by Ma and Zhu
(2013) <doi:10.1111/j.1751-5823.2012.00182.x> if you are interested in
statistical approach, or Engel, Huttenberger, and Hamann (2012)
<doi:10.4230/OASIcs.VLUDS.2011.135> for a broader multi-disciplinary
overview.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
