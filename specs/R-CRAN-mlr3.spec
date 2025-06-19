%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning in R - Next Generation

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-backports >= 1.5.0
BuildRequires:    R-CRAN-future.apply >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-paradox >= 1.0.1
BuildRequires:    R-CRAN-mlr3measures >= 1.0.0
BuildRequires:    R-CRAN-lgr >= 0.3.4
BuildRequires:    R-CRAN-mlr3misc >= 0.17.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-palmerpenguins 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-backports >= 1.5.0
Requires:         R-CRAN-future.apply >= 1.5.0
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-paradox >= 1.0.1
Requires:         R-CRAN-mlr3measures >= 1.0.0
Requires:         R-CRAN-lgr >= 0.3.4
Requires:         R-CRAN-mlr3misc >= 0.17.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-future 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-palmerpenguins 
Requires:         R-CRAN-uuid 

%description
Efficient, object-oriented programming on the building blocks of machine
learning. Provides 'R6' objects for tasks, learners, resamplings, and
measures. The package is geared towards scalability and larger datasets by
supporting parallelization and out-of-memory data-backends like databases.
While 'mlr3' focuses on the core computational operations, add-on packages
provide additional functionality.

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
