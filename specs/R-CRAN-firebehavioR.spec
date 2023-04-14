%global __brp_check_rpaths %{nil}
%global packname  firebehavioR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Prediction of Wildland Fire Behavior and Hazard

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-utils 

%description
Fire behavior prediction models, including the Scott & Reinhardt's (2001)
Rothermel Wildland Fire Modelling System <DOI:10.2737/RMRS-RP-29> and
Alexander et al.'s (2006) Crown Fire Initiation & Spread model
<DOI:10.1016/j.foreco.2006.08.174>. Also contains sample datasets,
estimation of fire behavior prediction model inputs (e.g., fuel moisture,
canopy characteristics, wind adjustment factor), results visualization,
and methods to estimate fire weather hazard.

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
