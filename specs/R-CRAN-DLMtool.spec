%global packname  DLMtool
%global packver   5.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.4.1
Release:          1%{?dist}
Summary:          Data-Limited Methods Toolkit

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-snowfall 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fmsb 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rfishbase 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-snowfall 
Requires:         R-CRAN-abind 
Requires:         R-boot 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fmsb 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-openxlsx 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rfishbase 
Requires:         R-CRAN-rmarkdown 
Requires:         R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Development, simulation testing, and implementation of management
procedures for data-limited fisheries (see Carruthers & Hordyk (2018)
<doi:10.1111/2041-210X.13081>).

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
