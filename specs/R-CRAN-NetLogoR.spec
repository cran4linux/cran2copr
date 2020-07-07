%global packname  NetLogoR
%global packver   0.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.7
Release:          3%{?dist}
Summary:          Build and Run Spatially Explicit Agent-Based Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-quickPlot >= 0.1.2
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-SpaDES.tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-quickPlot >= 0.1.2
Requires:         R-CRAN-raster 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-car 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-SpaDES.tools 
Requires:         R-stats 
Requires:         R-CRAN-rgeos 

%description
Build and run spatially explicit agent-based models using only the R
platform. 'NetLogoR' follows the same framework as the 'NetLogo' software
(Wilensky, 1999 <http://ccl.northwestern.edu/netlogo/>) and is a
translation in R of the structure and functions of 'NetLogo'. 'NetLogoR'
provides new R classes to define model agents and functions to implement
spatially explicit agent-based models in the R environment. This package
allows benefiting of the fast and easy coding phase from the highly
developed 'NetLogo' framework, coupled with the versatility, power and
massive resources of the R software. Examples of three models (Ants
<http://ccl.northwestern.edu/netlogo/models/Ants>, Butterfly (Railsback
and Grimm, 2012) and Wolf-Sheep-Predation
<http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation>) written
using 'NetLogoR' are available. The 'NetLogo' code of the original version
of these models is provided alongside. A programming guide inspired from
the 'NetLogo' Programming Guide
(<https://ccl.northwestern.edu/netlogo/docs/programming.html>) and a
dictionary of 'NetLogo' primitives
(<https://ccl.northwestern.edu/netlogo/docs/dictionary.html>) equivalences
are also available. NOTE: To increment 'time', these functions can use a
for loop or can be integrated with a discrete event simulator, such as
'SpaDES' (<https://cran.r-project.org/package=SpaDES>). The suggested
package 'fastshp' can be installed with 'install.packages("fastshp", repos
= "https://rforge.net", type = "source")'.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
