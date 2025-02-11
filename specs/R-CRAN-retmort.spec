%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  retmort
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate User-Based Tagging Mortality and Tag Loss in Mark-Recapture Studies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rmarkdown 

%description
We provide several avenues to predict and account for user-based mortality
and tag loss during mark-recapture studies. When planning a study on a
target species, the retentionmort_generation() function can be used to
produce multiple synthetic mark-recapture datasets to anticipate the error
associated with a planned field study to guide method development to
reduce error. Similarly, if field data was already collected, the
retentionmort() function can be used to predict the error from already
generated data to adjust for user-based mortality and tag loss. The
test_dataset_retentionmort() function will provide an example dataset of
how data should be inputted into the function to run properly. Lastly, the
retentionmort_figure() function can be used on any dataset generated from
either model function to produce an 'rmarkdown' printout of preliminary
analysis associated with the model, including summary statistics and
figures. Methods and results pertaining to the formation of this package
can be found in McCutcheon et al. (in review, "Predicting tagging-related
mortality and tag loss during mark-recapture studies").

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
