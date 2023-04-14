%global __brp_check_rpaths %{nil}
%global packname  tsoutliers
%global packver   0.6-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.8
Release:          3%{?dist}%{?buildtag}
Summary:          Detection of Outliers in Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-stats 

%description
Detection of outliers in time series following the Chen and Liu (1993)
<DOI:10.2307/2290724> procedure. Innovational outliers, additive outliers,
level shifts, temporary changes and seasonal level shifts are considered.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
