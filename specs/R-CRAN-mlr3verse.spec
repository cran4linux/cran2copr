%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3verse
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'mlr3' Package Family

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbotk >= 1.5.0
BuildRequires:    R-CRAN-mlr3tuning >= 1.3.0
BuildRequires:    R-CRAN-mlr3fselect >= 1.2.1
BuildRequires:    R-CRAN-paradox >= 1.0.1
BuildRequires:    R-CRAN-mlr3data >= 0.9.0
BuildRequires:    R-CRAN-mlr3learners >= 0.9.0
BuildRequires:    R-CRAN-mlr3filters >= 0.8.1
BuildRequires:    R-CRAN-mlr3pipelines >= 0.7.1
BuildRequires:    R-CRAN-mlr3hyperband >= 0.6.0
BuildRequires:    R-CRAN-mlr3tuningspaces >= 0.5.2
BuildRequires:    R-CRAN-mlr3 >= 0.20.0
BuildRequires:    R-CRAN-mlr3mbo >= 0.2.8
BuildRequires:    R-CRAN-mlr3misc >= 0.16.0
BuildRequires:    R-CRAN-mlr3viz >= 0.10.0
BuildRequires:    R-CRAN-mlr3cluster >= 0.1.10
BuildRequires:    R-CRAN-mlr3inferr >= 0.1.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-bbotk >= 1.5.0
Requires:         R-CRAN-mlr3tuning >= 1.3.0
Requires:         R-CRAN-mlr3fselect >= 1.2.1
Requires:         R-CRAN-paradox >= 1.0.1
Requires:         R-CRAN-mlr3data >= 0.9.0
Requires:         R-CRAN-mlr3learners >= 0.9.0
Requires:         R-CRAN-mlr3filters >= 0.8.1
Requires:         R-CRAN-mlr3pipelines >= 0.7.1
Requires:         R-CRAN-mlr3hyperband >= 0.6.0
Requires:         R-CRAN-mlr3tuningspaces >= 0.5.2
Requires:         R-CRAN-mlr3 >= 0.20.0
Requires:         R-CRAN-mlr3mbo >= 0.2.8
Requires:         R-CRAN-mlr3misc >= 0.16.0
Requires:         R-CRAN-mlr3viz >= 0.10.0
Requires:         R-CRAN-mlr3cluster >= 0.1.10
Requires:         R-CRAN-mlr3inferr >= 0.1.0
Requires:         R-CRAN-data.table 

%description
The 'mlr3' package family is a set of packages for machine-learning
purposes built in a modular fashion. This wrapper package is aimed to
simplify the installation and loading of the core 'mlr3' packages. Get
more information about the 'mlr3' project at
<https://mlr3book.mlr-org.com/>.

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
