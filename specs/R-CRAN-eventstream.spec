%global __brp_check_rpaths %{nil}
%global packname  eventstream
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Streaming Events and their Early Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensorA 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensorA 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-dplyr 

%description
Implements event extraction and early classification of events in data
streams in R. It has the functionality to generate 2-dimensional data
streams with events belonging to 2 classes. These events can be extracted
and features computed. The event features extracted from incomplete-events
can be classified using a partial-observations-classifier (Kandanaarachchi
et al. 2018) <doi:10.1371/journal.pone.0236331>.

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
