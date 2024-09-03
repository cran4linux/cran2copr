%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuICSeedR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Data for Fluorophore-Assisted Seed Amplification Assays

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-WRS2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-WRS2 
Requires:         R-CRAN-magrittr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-readxl 

%description
A toolkit for analysis and visualization of data from fluorophore-assisted
seed amplification assays, such as Real-Time Quaking-Induced Conversion
(RT-QuIC) and Fluorophore-Assisted Protein Misfolding Cyclic Amplification
(PMCA). 'QuICSeedR' addresses limitations in existing software by
automating data processing, supporting large-scale analysis, and enabling
comparative studies of analysis methods. It incorporates methods described
in Henderson et al. (2015) <doi:10.1099/vir.0.069906-0>, Li et al. (2020)
<doi:10.1038/s41598-021-96127-8>, Rowden et al. (2023)
<doi:10.3390/pathogens12020309>, Haley et al. (2013)
<doi:10.1371/journal.pone.0081488>, and Mair and Wilcox (2020)
<doi:10.3758/s13428-019-01246-w>. Please refer to the original
publications for details.

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
