%global packname  StratigrapheR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Integrated Stratigraphy

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-diagram 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-XML 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-diagram 

%description
Includes bases for litholog generation: graphical functions based on R
base graphics, interval management functions and svg importation functions
among others. Also include stereographic projection functions, and other
functions made to deal with large datasets while keeping options to get
into the details of the data. When using for publication please cite
Wouters, S., Da Silva, A.C. Crucifix, M., Sinnesael, M., Zivanovic, M.,
Boulvain, F., Devleeschouwer, X., 2019, Litholog generation with the
StratigrapheR package and signal decomposition for cyclostratigraphic
purposes. Geophysical Research Abstracts Vol. 21, EGU2019-5520, 2019, EGU
General Assembly 2019. <http://hdl.handle.net/2268/234402> The
palaeomagnetism functions are based on: Tauxe, L., 2010. Essentials of
Paleomagnetism. University of California Press.
<https://earthref.org/MagIC/books/Tauxe/Essentials/>; Allmendinger, R. W.,
Cardozo, N. C., and Fisher, D., 2013, Structural Geology Algorithms:
Vectors & Tensors: Cambridge, England, Cambridge University Press, 289
pp.; Cardozo, N., and Allmendinger, R. W., 2013, Spherical projections
with OSXStereonet: Computers & Geosciences, v. 51, no. 0, p. 193 - 205,
<doi: 10.1016/j.cageo.2012.07.021>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
