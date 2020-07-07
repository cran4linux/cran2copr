%global packname  KarsTS
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          2%{?dist}
Summary:          An Interface for Microclimate Time Series Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-MVN 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-tseriesChaos 
BuildRequires:    R-CRAN-stlplus 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-stinepack 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-nonlinearTseries 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-MVN 
Requires:         R-tcltk 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-tseriesChaos 
Requires:         R-CRAN-stlplus 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-stinepack 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-nonlinearTseries 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-grDevices 
Requires:         R-CRAN-rgl 
Requires:         R-mgcv 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-plot3D 

%description
An R code with a GUI for microclimate time series, with an emphasis on
underground environments. 'KarsTS' provides linear and nonlinear methods,
including recurrence analysis (Marwan et al. (2007)
<10.1016/j.physrep.2006.11.001>) and filling methods (Moffat et al. (2007)
<doi:10.1016/j.agrformet.2007.08.011>), as well as tools to manipulate
easily time series and gap sets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
