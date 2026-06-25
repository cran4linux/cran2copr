%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dataProfilerR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Exploratory Data Analysis and Dataset Profiling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
Profiles a data frame with minimal input: column type inference,
missing-value analysis, distributional summary statistics (including
skewness and kurtosis), normality tests, outlier detection, correlation
and categorical-association analysis, date-column profiling, grouped
comparisons and an overall data-quality score, alongside a set of
'ggplot2' visualisations. A single entry point, profile_data(), returns a
structured S3 object holding metadata, statistics, diagnostics and plots,
with print(), summary() and plot() methods, and report() renders the whole
profile to a self-contained HTML file. Statistical methods include the
Shapiro-Wilk normality test as implemented by Royston (1995)
<doi:10.2307/2986146> and the Anderson-Darling test following Stephens
(1974) <doi:10.1080/01621459.1974.10480196>, with power comparisons of
these tests in Yap and Sim (2011) <doi:10.1080/00949655.2010.520163>, and
the categorical association measure of Cramer (1946, ISBN:9780691080048).

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
