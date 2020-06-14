%global packname  VOSONDash
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          2%{?dist}
Summary:          User Interface for Collecting and Analysing Social Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.3.2
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-vosonSML >= 0.29.0
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wordcloud 
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-vosonSML >= 0.29.0
Requires:         R-graphics 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-lattice 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-syuzhet 
Requires:         R-CRAN-tm 
Requires:         R-utils 
Requires:         R-CRAN-wordcloud 

%description
A 'Shiny' application for the interactive visualisation and analysis of
networks that also provides a web interface for collecting social media
data using 'vosonSML'.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vosondash
%{rlibdir}/%{packname}/INDEX
