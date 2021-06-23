%global __brp_check_rpaths %{nil}
%global packname  VOSONDash
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}%{?buildtag}
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
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-syuzhet 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-wordcloud 
Requires:         R-CRAN-shiny >= 1.3.2
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-vosonSML >= 0.29.0
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-httr 
Requires:         R-lattice 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-syuzhet 
Requires:         R-CRAN-textutils 
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
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
