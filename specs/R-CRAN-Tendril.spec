%global __brp_check_rpaths %{nil}
%global packname  Tendril
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Compute and Display Tendril Plots

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plotly 

%description
Compute the coordinates to produce a tendril plot. In the tendril plot,
each tendril (branch) represents a type of events, and the direction of
the tendril is dictated by on which treatment arm the event is occurring.
If an event is occurring on the first of the two specified treatment arms,
the tendril bends in a clockwise direction. If an event is occurring on
the second of the treatment arms, the tendril bends in an anti-clockwise
direction. Ref: Karpefors, M and Weatherall, J., "The Tendril Plot - a
novel visual summary of the incidence, significance and temporal aspects
of adverse events in clinical trials" - JAMIA 2018; 25(8): 1069-1073
<doi:10.1093/jamia/ocy016>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
