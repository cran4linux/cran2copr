%global packname  VOSONDash
%global packver   0.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          User Interface for Collecting and Analysing Social Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-rtweet >= 0.6.8
BuildRequires:    R-CRAN-vosonSML >= 0.27.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-httpuv 
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-rtweet >= 0.6.8
Requires:         R-CRAN-vosonSML >= 0.27.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-wordcloud 
Requires:         R-CRAN-syuzhet 
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-CRAN-httpuv 

%description
A 'Shiny' application for the interactive visualisation and analysis of
networks that also provides a web interface for collecting social media
data using 'vosonSML'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vosondash
%{rlibdir}/%{packname}/INDEX
