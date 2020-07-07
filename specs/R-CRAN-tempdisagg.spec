%global packname  tempdisagg
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Methods for Temporal Disaggregation and Interpolation of TimeSeries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Temporal disaggregation methods are used to disaggregate and interpolate a
low frequency time series to a higher frequency series, where either the
sum, the mean, the first or the last value of the resulting high frequency
series is consistent with the low frequency series. Temporal
disaggregation can be performed with or without one or more high frequency
indicator series. Contains the methods of Chow-Lin, Santos-Silva-Cardoso,
Fernandez, Litterman, Denton and Denton-Cholette, summarized in Sax and
Steiner (2013) <doi:10.32614/RJ-2013-028>. Supports most R time series
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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/prepare
%{rlibdir}/%{packname}/INDEX
