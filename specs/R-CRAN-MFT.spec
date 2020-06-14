%global packname  MFT
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          2%{?dist}
Summary:          The Multiple Filter Test for Change Point Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides statistical tests and algorithms for the detection of change
points in time series and point processes - particularly for changes in
the mean in time series and for changes in the rate and in the variance in
point processes. References - Michael Messer, Marietta Kirchner, Julia
Schiemann, Jochen Roeper, Ralph Neininger and Gaby Schneider (2014), A
multiple filter test for the detection of rate changes in renewal
processes with varying variance <doi:10.1214/14-AOAS782>. Stefan Albert,
Michael Messer, Julia Schiemann, Jochen Roeper, Gaby Schneider (2017),
Multi-scale detection of variance changes in renewal processes in the
presence of rate change points <doi:10.1111/jtsa.12254>. Michael Messer,
Kaue M. Costa, Jochen Roeper and Gaby Schneider (2017), Multi-scale
detection of rate changes in spike trains with weak dependencies
<doi:10.1007/s10827-016-0635-3>. Michael Messer, Stefan Albert and Gaby
Schneider (2018), The multiple filter test for change point detection in
time series <doi:10.1007/s00184-018-0672-1>. Michael Messer, Hendrik
Backhaus, Albrecht Stroh and Gaby Schneider (2019+) Peak detection in time
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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
