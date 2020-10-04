%global packname  kgc
%global packver   1.0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Koeppen-Geiger Climatic Zones

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-plyr 

%description
Aids in identifying the Koeppen-Geiger (KG) climatic zone for a given
location. The Koeppen-Geiger climate zones were first published in 1884,
as a system to classify regions of the earth by their relative heat and
humidity through the year, for the benefit of human health, plant and
agriculture and other human activity [1]. This climate zone classification
system, applicable to all of the earths surface, has continued to be
developed by scientists up to the present day.  Recently one of use (FZ)
has published updated, higher accuracy KG climate zone definitions [2]. In
this package we use these updated high-resolution maps as the data source
[3]. We provide functions that return the KG climate zone for a given
longitude and lattitude, or for a given United States zip code. In
addition the CZUncertainty() function will check climate zones nearby to
check if the given location is near a climate zone boundary. In addition
an interactive shiny app is provided to define the KG climate zone for a
given longitude and lattitude, or United States zip code. Digital data, as
well as animated maps, showing the shift of the climate zones are provided
on the following website <http://koeppen-geiger.vu-wien.ac.at>. This work
was supported by the DOE-EERE SunShot award DE-EE-0007140. [1] W. Koeppen,
(2011) <doi:10.1127/0941-2948/2011/105>. [2] F. Rubel and M. Kottek,
(2010) <doi:10.1127/0941-2948/2010/0430>. [3] F. Rubel, K. Brugger, K.
Haslinger, and I. Auer, (2016) <doi:10.1127/metz/2016/0816>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/exdata
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
