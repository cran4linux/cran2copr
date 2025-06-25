%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eq5dsuite
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Handling and Analysing EQ-5d Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rappdirs 

%description
The EQ-5D is a widely-used standarized instrument for measuring Health
Related Quality Of Life (HRQOL), developed by the EuroQol group
<https://euroqol.org/>. It assesses five dimensions; mobility, self-care,
usual activities, pain/discomfort, and anxiety/depression, using either a
three-level (EQ-5D-3L) or five-level (EQ-5D-5L) scale. Scores from these
dimensions are commonly converted into a single utility index using
country-specific value sets, which are critical in clinical and economic
evaluations of healthcare and in population health surveys. The eq5dsuite
package enables users to calculate utility index values for the EQ-5D
instruments, including crosswalk utilities using the original crosswalk
developed by van Hout et al. (2012) <doi:10.1016/j.jval.2012.02.008>
(mapping EQ-5D-5L responses to EQ-5D-3L index values), or the recently
developed reverse crosswalk by van Hout et al. (2021)
<doi:10.1016/j.jval.2021.03.009> (mapping EQ-5D-3L responses to EQ-5D-5L
index values). Users are allowed to add and/or remove user-defined value
sets. Additionally, the package provides tools to analyze EQ-5D data
according to the recommended guidelines outlined in "Methods for Analyzing
and Reporting EQ-5D data" by Devlin et al. (2020)
<doi:10.1007/978-3-030-47622-9>.

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
