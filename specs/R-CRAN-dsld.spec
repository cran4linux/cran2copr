%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsld
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Science Looks at Discrimination

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fairml 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-regtools 
BuildRequires:    R-CRAN-qeML 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-freqparcoord 
BuildRequires:    R-CRAN-fairness 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-fairml 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-regtools 
Requires:         R-CRAN-qeML 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-freqparcoord 
Requires:         R-CRAN-fairness 
Requires:         R-CRAN-sandwich 

%description
Statistical and graphical tools for detecting and measuring discrimination
and bias, be it racial, gender, age or other. Detection and remediation of
bias in machine learning algorithms. 'Python' interfaces available.

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
