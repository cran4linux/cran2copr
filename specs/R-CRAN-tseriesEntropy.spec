%global packname  tseriesEntropy
%global packver   0.6-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          Entropy Based Analysis and Tests for Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ks 
Requires:         R-CRAN-cubature 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ks 

%description
Implements an Entropy measure of dependence based on the
Bhattacharya-Hellinger-Matusita distance. Can be used as a (nonlinear)
autocorrelation/crosscorrelation function for continuous and categorical
time series. The package includes tests for serial dependence and
nonlinearity based on it. Some routines have a parallel version that can
be used in a multicore/cluster environment. The package makes use of S4
classes.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
