%global packname  DLMtool
%global packver   5.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.4.3
Release:          1%{?dist}
Summary:          Data-Limited Methods Toolkit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Development, simulation testing, and implementation of management
procedures for data-limited fisheries (see Carruthers & Hordyk (2018)
<doi:10.1111/2041-210X.13081>).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/Atlantic_mackerel.csv
%doc %{rlibdir}/%{packname}/China_rockfish.csv
%doc %{rlibdir}/%{packname}/Cobia.csv
%doc %{rlibdir}/%{packname}/Data_Example.csv
%doc %{rlibdir}/%{packname}/Data_Example.md
%doc %{rlibdir}/%{packname}/Data_Example.xlsx
%doc %{rlibdir}/%{packname}/Data.csv
%doc %{rlibdir}/%{packname}/Data.xlsx
%doc %{rlibdir}/%{packname}/DFO_cosewic.Rmd
%doc %{rlibdir}/%{packname}/DFO_generic.Rmd
%doc %{rlibdir}/%{packname}/Example_Chile_Hake.rmd
%doc %{rlibdir}/%{packname}/Example_Chile_Hake.xlsx
%{rlibdir}/%{packname}/Example_datafile.csv
%doc %{rlibdir}/%{packname}/Gulf_blue_tilefish.csv
%doc %{rlibdir}/%{packname}/OM.rmd
%doc %{rlibdir}/%{packname}/OM.xlsx
%doc %{rlibdir}/%{packname}/ourReefFish.csv
%doc %{rlibdir}/%{packname}/PLimitTable.Rmd
%doc %{rlibdir}/%{packname}/PLimitTable2.Rmd
%doc %{rlibdir}/%{packname}/PObjTable.Rmd
%doc %{rlibdir}/%{packname}/PObjTable2.Rmd
%doc %{rlibdir}/%{packname}/Red_snapper.csv
%doc %{rlibdir}/%{packname}/Rmd
%doc %{rlibdir}/%{packname}/Simulation_1.csv
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
