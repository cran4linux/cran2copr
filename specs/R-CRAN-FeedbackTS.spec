%global packname  FeedbackTS
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          2%{?dist}
Summary:          Analysis of Feedback in Time Series

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-proj4 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-automap 
Requires:         R-methods 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-proj4 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-automap 

%description
Analysis of fragmented time directionality to investigate feedback in time
series. Tools provided by the package allow the analysis of feedback for a
single time series and the analysis of feedback for a set of time series
collected across a spatial domain.

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
