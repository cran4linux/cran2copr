%global packname  iSTATS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          A Graphical Interface to Perform STOCSY Analyses on NMR Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.8.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-Cairo >= 1.5
BuildRequires:    R-CRAN-shiny >= 1.0.2
BuildRequires:    R-CRAN-shinyBS >= 0.61
BuildRequires:    R-CRAN-shinyWidgets >= 0.4.3
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-gtools >= 3.8.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-Cairo >= 1.5
Requires:         R-CRAN-shiny >= 1.0.2
Requires:         R-CRAN-shinyBS >= 0.61
Requires:         R-CRAN-shinyWidgets >= 0.4.3
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-data.table 

%description
Launches a 'shiny' based application for Nuclear Magnetic Resonance (NMR)
data importation and Statistical TOtal Correlation SpectroscopY (STOCSY)
analyses in a full interactive approach. The theoretical background and
applications of STOCSY method could be found at Cloarec, O., Dumas, M. E.,
Craig, A., Barton, R. H., Trygg, J., Hudson, J., Blancher, C., Gauguier,
D., Lindon, J. C., Holmes, E. & Nicholson, J. (2005)
<doi:10.1021/ac048630x>.

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
%doc %{rlibdir}/%{packname}/app
%{rlibdir}/%{packname}/INDEX
