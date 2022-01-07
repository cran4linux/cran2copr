%global __brp_check_rpaths %{nil}
%global packname  postGGIR
%global packver   2.4.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Data Processing after Running 'GGIR' for Accelerometer Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-refund 
BuildRequires:    R-CRAN-denseFLMM 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-cosinor 
BuildRequires:    R-CRAN-cosinor2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-accelerometry 
BuildRequires:    R-CRAN-ActCR 
BuildRequires:    R-CRAN-ActFrag 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-GGIR 
Requires:         R-CRAN-refund 
Requires:         R-CRAN-denseFLMM 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-cosinor 
Requires:         R-CRAN-cosinor2 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-accelerometry 
Requires:         R-CRAN-ActCR 
Requires:         R-CRAN-ActFrag 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-GGIR 

%description
Generate all necessary R/Rmd/shell files for data processing after running
'GGIR' (v2.4.0) for accelerometer data. In part 1, all csv files in the
GGIR output directory were read, transformed and then merged. In part 2,
the GGIR output files were checked and summarized in one excel sheet. In
part 3, the merged data was cleaned according to the number of valid hours
on each night and the number of valid days for each subject. In part 4,
the cleaned activity data was imputed by the average Euclidean norm minus
one (ENMO) over all the valid days for each subject. Finally, a
comprehensive report of data processing was created using Rmarkdown, and
the report includes few exploratory plots and multiple commonly used
features extracted from minute level actigraphy data.

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
