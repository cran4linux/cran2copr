%global __brp_check_rpaths %{nil}
%global packname  ggsn
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          North Symbols and Scale Bars for Maps Created with 'ggplot2' or'ggmap'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-png 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-ggmap 
Requires:         R-graphics 
Requires:         R-utils 

%description
Adds north symbols (18 options) and scale bars in kilometers, meters,
nautical miles, or statue miles, to maps in geographic or metric
coordinates created with 'ggplot2' or 'ggmap'.

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
