%global packname  stepR
%global packver   2.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          Multiscale Change-Point Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-digest >= 0.6.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-R.cache >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
Requires:         R-CRAN-digest >= 0.6.10
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-R.cache >= 0.10.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 

%description
Allows fitting of step-functions to univariate serial data where neither
the number of jumps nor their positions is known by implementing the
multiscale regression estimators SMUCE (K. Frick, A. Munk and H. Sieling,
2014) <doi:10.1111/rssb.12047> and HSMUCE (F. Pein, H. Sieling and A.
Munk, 2017) <doi:10.1111/rssb.12202>. In addition, confidence intervals
for the change-point locations and bands for the unknown signal can be
obtained.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
