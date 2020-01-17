%global packname  SparseMSE
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          'Multiple Systems Estimation for Sparse Capture Data'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rcapture 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rcapture 

%description
Implements the routines and algorithms developed and analysed in "Multiple
Systems Estimation for Sparse Capture Data: Inferential Challenges when
there are Non-Overlapping Lists" Chan, L, Silverman, B. W., Vincent, K
(2019) <arXiv:1902.05156>. This package explicitly handles situations
where there are pairs of lists which have no observed individuals in
common.  It deals correctly with parameters whose estimated values can be
considered as being negative infinity.  It also addresses other possible
issues of non-existence and non-identifiability of maximum likelihood
estimates.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
