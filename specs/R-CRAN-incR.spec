%global __brp_check_rpaths %{nil}
%global packname  incR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Incubation Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-utils 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rgeos 
Requires:         R-utils 

%description
Suite of functions to study animal incubation. At the core of incR lies an
algorithm that allows for the scoring of incubation behaviour.
Additionally, several functions extract biologically relevant metrics of
incubation such as off-bout number and off-bout duration - for a review of
avian incubation studies, see Nests, Eggs, and Incubation: New ideas about
avian reproduction (2015) edited by D. Charles Deeming and S. James
Reynolds <doi:10.1093/acprof:oso/9780198718666.001.0001>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
