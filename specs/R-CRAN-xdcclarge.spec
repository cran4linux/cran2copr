%global packname  xdcclarge
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Estimating a (c)DCC-GARCH Model in Large Dimensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.34
BuildRequires:    R-CRAN-Rcpp >= 0.10.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nlshrink 
Requires:         R-CRAN-Rcpp >= 0.10.6
Requires:         R-stats 
Requires:         R-CRAN-nlshrink 

%description
Functions for Estimating a (c)DCC-GARCH Model in large dimensions based on
a publication by Engle et,al (2017) <doi:10.1080/07350015.2017.1345683>
and Nakagawa et,al (2018) <doi:10.3390/ijfs6020052>. This estimation
method is consist of composite likelihood method by Pakel et al. (2014)
<http://paneldataconference2015.ceu.hu/Program/Cavit-Pakel.pdf> and
(Non-)linear shrinkage estimation of covariance matrices by Ledoit and
Wolf (2004,2015,2016). (<doi:10.1016/S0047-259X(03)00096-4>,
<doi:10.1214/12-AOS989>, <doi:10.1016/j.jmva.2015.04.006>).

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
%{rlibdir}/%{packname}/libs
