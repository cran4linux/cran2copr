%global packname  NlinTS
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          1%{?dist}
Summary:          Non Linear Time Series Analysis

License:          GNU General Public License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-Rdpack 

%description
Models for non-linear time series analysis and causality detection.  The
main functionalities of this package consist of an implementation of the
classical causality test (C.W.J.Granger 1980)
<doi:10.1016/0165-1889(80)90069-X>, and a non-linear version of it based
on feed-forward neural networks. This package contains also an
implementation of the Transfer Entropy <doi:10.1103/PhysRevLett.85.461>,
and the continuous Transfer Entropy using an approximation based on the
k-nearest neighbors <doi:10.1103/PhysRevE.69.066138>. There are also some
other useful tools, like the VARNN (Vector Auto-Regressive Neural Network)
prediction model, the Augmented test of stationarity, and the discrete and
continuous entropy and mutual information.

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
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
