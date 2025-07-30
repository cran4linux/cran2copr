%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyrhrv
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read, Iteratively Filter, and Analyze Multiple ECG Datasets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RHRV 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-RHRV 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-grDevices 

%description
Allows users to quickly load multiple patients' electrocardiographic (ECG)
data at once and conduct relevant time analysis of heart rate variability
(HRV) without manual edits from a physician or data cleaning specialist.
The package provides the unique ability to iteratively filter, plot, and
store time analysis results in a data frame while writing plots to a
predefined folder. This streamlines the workflow for HRV analysis across
multiple datasets. Methods are based on Rodríguez-Liñares et al. (2011)
<doi:10.1016/j.cmpb.2010.05.012>. Examples of applications using this
package include Kwon et al. (2022) <doi:10.1007/s10286-022-00865-2> and
Lawrence et al. (2023) <doi:10.1016/j.autneu.2022.103056>.

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
