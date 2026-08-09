%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EDAForge
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Exploratory Data Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-visdat 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-visdat 
Requires:         R-CRAN-igraph 

%description
Automatically performs exploratory data analysis (EDA) for tabular
datasets, including data summaries, missing value analysis, descriptive
statistics, visualizations, correlation analysis, outlier detection, and
automated report generation. The package provides a streamlined workflow
for rapid data exploration and produces publication-ready tables and
graphics. For methodological details see Tukey (1977, ISBN:9780201076165),
Pearson (1895) <doi:10.1098/rspl.1895.0041>, and Wickham (2014)
<doi:10.18637/jss.v059.i10>.

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
