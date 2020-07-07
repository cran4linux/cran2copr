%global packname  yakmoR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          A Simple Wrapper for the k-Means Library Yakmo

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-BBmisc >= 1.9
BuildRequires:    R-CRAN-checkmate >= 1.5.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
Requires:         R-CRAN-BBmisc >= 1.9
Requires:         R-CRAN-checkmate >= 1.5.1
Requires:         R-CRAN-Rcpp >= 0.11.6

%description
This is a simple wrapper for the yakmo K-Means library (developed by Naoki
Yoshinaga, see http://www.tkl.iis.u-tokyo.ac.jp/~ynaga/yakmo/). It
performs fast and robust (orthogonal) K-Means.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
