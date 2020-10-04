%global packname  scPDSI
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of the Conventional and Self-Calibrating PalmerDrought Severity Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-stats 

%description
Calculating the monthly conventional and self-calibrating Palmer Drought
Severity Index (PDSI and scPDSI) using the precipitation and potential
evapotranspiration data. The function to calculate PDSI is based on the
C++ source codes developed by Nathan Wells, Steve Goddard and Michael J.
Hayes, University of Nebraska-Lincoln. Reference: Palmer W. (1965).
Meteorological drought. U.s.department of Commerce Weather Bureau Research
Paper,
<https://www.ncdc.noaa.gov/temp-and-precip/drought/docs/palmer.pdf>; Wells
N., Goddard S., Hayes M. J. (2004). A Self-Calibrating Palmer Drought
Severity Index. Journal of Climate, 17(12):2335-2351,
<DOI:10.1175/1520-0442(2004)017%3C2335:ASPDSI%3E2.0.CO;2>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
