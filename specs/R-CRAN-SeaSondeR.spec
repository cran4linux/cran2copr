%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeaSondeR
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Radial Metrics from SeaSonde HF-Radar Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bit64 >= 4.0.5
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-pracma >= 2.4.4
BuildRequires:    R-CRAN-yaml >= 2.3.7
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-lubridate >= 1.9.3
BuildRequires:    R-CRAN-zoo >= 1.8.12
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-geosphere >= 1.5.18
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-uuid >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-bitops >= 1.0.7
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-constants >= 1.0.1
BuildRequires:    R-CRAN-whisker >= 0.4.1
BuildRequires:    R-CRAN-slider >= 0.3.1
Requires:         R-CRAN-bit64 >= 4.0.5
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-pracma >= 2.4.4
Requires:         R-CRAN-yaml >= 2.3.7
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-lubridate >= 1.9.3
Requires:         R-CRAN-zoo >= 1.8.12
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-geosphere >= 1.5.18
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-uuid >= 1.2.1
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-bitops >= 1.0.7
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-constants >= 1.0.1
Requires:         R-CRAN-whisker >= 0.4.1
Requires:         R-CRAN-slider >= 0.3.1

%description
Read CODAR's SeaSonde High-Frequency Radar spectra files, compute radial
metrics, and generate plots for spectra and antenna pattern data.
Implementation is based in technical manuals, publications and patents,
please refer to the following documents for more information: Barrick and
Lipa (1999) <https://codar.com/images/about/patents/05990834.PDF>; CODAR
Ocean Sensors (2002)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Docs/Informative/FirstOrder_Settings.pdf>;
Lipa et al. (2006) <doi:10.1109/joe.2006.886104>; Paolo et al. (2007)
<doi:10.1109/oceans.2007.4449265>; CODAR Ocean Sensors (2009a)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Docs/GuidesToFileFormats/File_AntennaPattern.pdf>;
CODAR Ocean Sensors (2009b)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Docs/GuidesToFileFormats/File_CrossSpectraReduced.pdf>;
CODAR Ocean Sensors (2016a)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Manuals_Documentation_Release_8/File_Formats/File_Cross_Spectra_V6.pdf>;
CODAR Ocean Sensors (2016b)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Manuals_Documentation_Release_8/File_Formats/FIle_Reduced_Spectra.pdf>;
CODAR Ocean Sensors (2016c)
<http://support.codar.com/Technicians_Information_Page_for_SeaSondes/Manuals_Documentation_Release_8/Application_Guides/Guide_SpectraPlotterMap.pdf>;
Bushnell and Worthington (2022) <doi:10.25923/4c5x-g538>.

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
