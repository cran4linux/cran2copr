%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GENEAclassify
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Segmentation and Classification of Accelerometer Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-GENEAread 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-rpart 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-GENEAread 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-rpart 

%description
Segmentation and classification procedures for data from the
'Activinsights GENEActiv'
<https://activinsights.com/technology/geneactiv/> accelerometer that
provides the user with a model to guess behaviour from test data where
behaviour is missing. Includes a step counting algorithm, a function to
create segmented data with custom features and a function to use recursive
partitioning provided in the function rpart() of the 'rpart' package to
create classification models.

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
