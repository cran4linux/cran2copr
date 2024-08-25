%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HDXBoxeR
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Hydrogen-Deuterium Exchange Mass-Spectrometry Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-wrapr 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-wrapr 

%description
A protocol that facilitates the processing and analysis of
Hydrogen-Deuterium Exchange Mass Spectrometry data using p-value
statistics and Critical Interval analysis. It provides a pipeline for
analyzing data from 'HDXExaminer' (Sierra Analytics, Trajan Scientific),
automating matching and comparison of protein states through Welch's
T-test and the Critical Interval statistical framework. Additionally, it
simplifies data export, generates 'PyMol' scripts, and ensures
calculations meet publication standards. 'HDXBoxeR' assists in various
aspects of hydrogen-deuterium exchange data analysis, including
reprocessing data, calculating parameters, identifying significant
peptides, generating plots, and facilitating comparison between protein
states. For details check papers by Hageman and Weis (2019)
<doi:10.1021/acs.analchem.9b01325> and Masson et al. (2019)
<doi:10.1038/s41592-019-0459-y>. 'HDXBoxeR' citation: Janowska et al.
(2024) <doi:10.1093/bioinformatics/btae479>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
