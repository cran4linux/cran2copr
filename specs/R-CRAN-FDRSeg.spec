%global packname  FDRSeg
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          FDR-Control in Multiscale Change-Point Segmentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.3
Requires:         R-core >= 2.15.3
BuildRequires:    R-CRAN-stepR >= 1.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-stats 
Requires:         R-CRAN-stepR >= 1.0.1
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-stats 

%description
Estimate step functions via multiscale inference with controlled false
discovery rate (FDR). For details see H. Li, A. Munk and H. Sieling (2016)
<doi:10.1214/16-EJS1131>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
