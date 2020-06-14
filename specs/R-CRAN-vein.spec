%global packname  vein
%global packver   0.8.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.9
Release:          2%{?dist}
Summary:          Vehicular Emissions Inventories

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-units 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Elaboration of vehicular emissions inventories, consisting in four stages,
pre-processing activity data, preparing emissions factors, estimating the
emissions and post-processing of emissions in maps and databases. More
details in Ibarra-Espinosa et al (2018) <doi:10.5194/gmd-11-2209-2018>.
Before using VEIN you need to know the vehicular composition of your study
area, in other words, the combination of of type of vehicles, size and
fuel of the fleet. Then, it is recommended to start with the project to
download a template to create a structure of directories and scripts.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/README.html
%doc %{rlibdir}/%{packname}/README.Rmd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
