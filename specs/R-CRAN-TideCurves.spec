%global __brp_check_rpaths %{nil}
%global packname  TideCurves
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis and Prediction of Tides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 9.9
BuildRequires:    R-CRAN-chron >= 2.3.54
BuildRequires:    R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-fields >= 9.9
Requires:         R-CRAN-chron >= 2.3.54
Requires:         R-CRAN-data.table >= 1.12.2

%description
Tidal analysis of evenly spaced observed time series (time step 1 to 60
min) with or without shorter gaps using the harmonic representation of
inequalities. The analysis should preferably cover an observation period
of at least 19 years. For shorter periods low frequency constituents are
not taken into account, in accordance with the Rayleigh-Criterion. The
main objective of this package is to synthesize or predict a tidal time
series.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
