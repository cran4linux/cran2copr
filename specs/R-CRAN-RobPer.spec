%global __brp_check_rpaths %{nil}
%global packname  RobPer
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Periodogram and Periodicity Detection Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-rgenoud 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-quantreg 
Requires:         R-splines 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-rgenoud 

%description
Calculates periodograms based on (robustly) fitting periodic functions to
light curves (irregularly observed time series, possibly with measurement
accuracies, occurring in astroparticle physics). Three main functions are
included: RobPer() calculates the periodogram. Outlying periodogram bars
(indicating a period) can be detected with betaCvMfit(). Artificial light
curves can be generated using the function tsgen(). For more details see
the corresponding article: Thieler, Fried and Rathjens (2016), Journal of
Statistical Software 69(9), 1-36, <doi:10.18637/jss.v069.i09>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
