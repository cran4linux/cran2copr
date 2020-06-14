%global packname  PhysicalActivity
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Process Accelerometer Data for Physical Activity Measurement

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
It provides a function "wearingMarking" for classification of monitor wear
and nonwear time intervals in accelerometer data collected to assess
physical activity. The package also contains functions for making plot for
accelerometer data and obtaining the summary of various information
including daily monitor wear time and the mean monitor wear time during
valid days. The revised package version 0.2-1 improved the functions in
the previous version regarding speed and robustness. In addition, several
functions were added: "markDelivery" can classify days for ActiGraph
delivery by mail; "markPAI" can categorize physical activity intensity
level based on user-defined cut-points of accelerometer counts. It also
supports importing ActiGraph AGD files with "readActigraph" and
"queryActigraph" functions. The package also better supports time zones
and daylight saving.

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
