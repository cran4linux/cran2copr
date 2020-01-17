%global packname  clampSeg
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Idealisation of Patch Clamp Recordings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-stepR >= 2.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-stepR >= 2.0.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-stats 
Requires:         R-methods 

%description
Allows for idealisation of patch clamp recordings by implementing the
non-parametric JUmp Local dEconvolution Segmentation (JULES) filter, see
F. Pein, I. Tecuapetla-Gómez, O. Schütte, C. Steinem, and A. Munk (2017)
<arXiv:1706.03671>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
