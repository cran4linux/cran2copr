%global packname  osmose
%global packver   3.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.4
Release:          3%{?dist}%{?buildtag}
Summary:          Object Oriented Simulator of Marine Ecosystems

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-rlist 
Requires:         R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-ncdf4 
Requires:         R-mgcv 
Requires:         R-CRAN-fields 

%description
The multispecies and individual-based model (IBM) 'OSMOSE' (Shin and Curry
(2001) <doi:10.1016/S0990-7440(01)01106-8> and Shin and Curry (2004)
<doi:10.1139/f03-154>) focuses on fish species. This model assumes
opportunistic predation based on spatial co-occurrence and size adequacy
between a predator and its prey (size-based opportunistic predation). It
represents fish individuals grouped into schools, which are characterized
by their size, weight, age, taxonomy and geographical location (2D model),
and which undergo major processes of fish life cycle (growth, explicit
predation, natural and starvation mortalities, reproduction and migration)
and fishing exploitation. The model needs basic biological parameters that
are often available for a wide range of species, and which can be found in
'FishBase' for instance (see <http://www.fishbase.org/search.php>), and
fish spatial distribution data. This package provides tools to build and
run simulations using the 'OSMOSE' model.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/reports
%{rlibdir}/%{packname}/INDEX
