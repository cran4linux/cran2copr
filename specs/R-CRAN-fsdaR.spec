%global __brp_check_rpaths %{nil}
%global packname  fsdaR
%global packver   0.6-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Data Analysis Through Monitoring and Dynamic Visualization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-methods 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-rJava 
Requires:         R-methods 
Requires:         R-stats4 
Requires:         R-CRAN-ggplot2 

%description
Provides interface to the 'MATLAB' toolbox 'Flexible Statistical Data
Analysis (FSDA)' which is comprehensive and computationally efficient
software package for robust statistics in regression, multivariate and
categorical data analysis. The current R version implements tools for
regression: (forward search, S- and MM-estimation, least trimmed squares
(LTS) and least median of squares (LMS)), for multivariate analysis
(forward search, S- and MM-estimation), for cluster analysis and
cluster-wise regression. The distinctive feature of our package is the
possibility of monitoring the statistics of interest as a function of
breakdown point, efficiency or subset size, depending on the estimator.
This is accompanied by a rich set of graphical features, such as dynamic
brushing, linking, particularly useful for exploratory data analysis.

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
