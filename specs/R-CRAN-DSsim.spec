%global packname  DSsim
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}
Summary:          Distance Sampling Simulations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mrds 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-shapefiles 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-mrds 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-splancs 
Requires:         R-mgcv 
Requires:         R-CRAN-shapefiles 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-sp 

%description
Performs distance sampling simulations.It repeatedly generates instances
of a user defined population within a given survey region, generates
realisations of a survey design (currently these must be generated using
Distance software in advance <http://distancesampling.org/>) and simulates
the detection process. The data are then analysed so that the results can
be compared for accuracy and precision across all replications. This will
allow users to select survey designs which will give them the best
accuracy and precision given their expectations about population
distribution. Any uncertainty in population distribution or population
parameters can be included by running the different survey designs for a
number of different population descriptions. An example simulation can be
found in the help file for make.simulation.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
