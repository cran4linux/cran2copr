%global packname  swephR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          High Precision Swiss Ephemeris

License:          AGPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
The Swiss Ephemeris (version 2.08) is a high precision ephemeris based
upon the DE431 ephemerides from NASA's JPL. It covers the time range 13201
BCE to 17191 CE. This package uses the semi-analytic theory by Steve
Moshier. For faster and more accurate calculations, the compressed Swiss
Ephemeris data is available in the 'swephRdata' package. To access this
data package, run 'install.packages("swephRdata", repos =
"https://rstub.github.io/drat/", type = "source")'. The size of the
'swephRdata' package is approximately 115 MB. The user can also use the
original JPL DE431 data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ephemeris
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
