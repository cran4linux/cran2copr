%global __brp_check_rpaths %{nil}
%global packname  soundClass
%global packver   0.0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sound Classification Using Convolutional Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shinyFiles 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-shinyjs 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-seewave 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shinyFiles 
Requires:         R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-shinyjs 

%description
Provides an all-in-one solution for automatic classification of sound
events using convolutional neural networks (CNN). The main purpose is to
provide a sound classification workflow, from annotating sound events in
recordings to training and automating model usage in real-life situations.
Using the package requires a pre-compiled collection of recordings with
sound events of interest and it can be employed for: 1) Annotation: create
a database of annotated recordings, 2) Training: prepare train data from
annotated recordings and fit CNN models, 3) Classification: automate the
use of the fitted model for classifying new recordings. By using automatic
feature selection and a user-friendly GUI for managing data and
training/deploying models, this package is intended to be used by a broad
audience as it does not require specific expertise in statistics,
programming or sound analysis. Please refer to the vignette for further
information. Gibb, R., et al. (2019) <doi:10.1111/2041-210X.13101> Mac
Aodha, O., et al. (2018) <doi:10.1371/journal.pcbi.1005995> Stowell, D.,
et al. (2019) <doi:10.1111/2041-210X.13103> LeCun, Y., et al. (2012)
<doi:10.1007/978-3-642-35289-8_3>.

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
