%global __brp_check_rpaths %{nil}
%global packname  TAShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          'Text Analyzer Shiny'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-wordcloud2 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-wordcloud2 

%description
Interactive shiny application for working with textmining and text
analytics. Various visualizations are provided.

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
