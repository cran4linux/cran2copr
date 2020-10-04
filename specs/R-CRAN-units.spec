%global packname  units
%global packver   0.6-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.7
Release:          3%{?dist}%{?buildtag}
Summary:          Measurement Units for R Vectors

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    udunits2-devel
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
Requires:         R-CRAN-Rcpp >= 0.12.10

%description
Support for measurement units in R vectors, matrices and arrays: automatic
propagation, conversion, derivation and simplification of units; raising
errors in case of unit incompatibility. Compatible with the POSIXct, Date
and difftime classes. Uses the UNIDATA udunits library and unit database
for unit compatibility checking and conversion. Documentation about
'units' is provided in the paper by Pebesma, Mailund & Hiebert (2016,
<doi:10.32614/RJ-2016-061>), included in this package as a vignette; see
'citation("units")' for details.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/share
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
