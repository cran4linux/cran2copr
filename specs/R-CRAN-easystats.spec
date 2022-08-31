%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  easystats
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Framework for Easy Statistical Modeling, Visualization, and Reporting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-performance >= 0.9.2
BuildRequires:    R-CRAN-modelbased >= 0.8.5
BuildRequires:    R-CRAN-correlation >= 0.8.2
BuildRequires:    R-CRAN-see >= 0.7.2
BuildRequires:    R-CRAN-effectsize >= 0.7.0.5
BuildRequires:    R-CRAN-datawizard >= 0.5.1
BuildRequires:    R-CRAN-report >= 0.5.1
BuildRequires:    R-CRAN-insight >= 0.18.2
BuildRequires:    R-CRAN-parameters >= 0.18.2
BuildRequires:    R-CRAN-bayestestR >= 0.12.1
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-performance >= 0.9.2
Requires:         R-CRAN-modelbased >= 0.8.5
Requires:         R-CRAN-correlation >= 0.8.2
Requires:         R-CRAN-see >= 0.7.2
Requires:         R-CRAN-effectsize >= 0.7.0.5
Requires:         R-CRAN-datawizard >= 0.5.1
Requires:         R-CRAN-report >= 0.5.1
Requires:         R-CRAN-insight >= 0.18.2
Requires:         R-CRAN-parameters >= 0.18.2
Requires:         R-CRAN-bayestestR >= 0.12.1
Requires:         R-tools 
Requires:         R-utils 

%description
A meta-package that installs and loads a set of packages from 'easystats'
ecosystem in a single step. This collection of packages provide a unifying
and consistent framework for statistical modeling, visualization, and
reporting. Additionally, it provides articles targeted at instructors for
teaching 'easystats', and a dashboard targeted at new R users for easily
conducting statistical analysis by accessing summary results, model fit
indices, and visualizations with minimal programming.

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
