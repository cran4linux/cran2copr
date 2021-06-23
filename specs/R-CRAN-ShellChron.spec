%global __brp_check_rpaths %{nil}
%global packname  ShellChron
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Builds Chronologies from Oxygen Isotope Profiles in Shells

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-zoo >= 1.8.7
BuildRequires:    R-CRAN-tidyverse >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-rtop >= 0.5.14
BuildRequires:    R-CRAN-ggpubr >= 0.4.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-zoo >= 1.8.7
Requires:         R-CRAN-tidyverse >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-rtop >= 0.5.14
Requires:         R-CRAN-ggpubr >= 0.4.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 

%description
Takes as input a stable oxygen isotope (d18O) profile measured in growth
direction (D) through a shell + uncertainties in both variables (d18O_err
& D_err). It then models the seasonality in the d18O record by fitting a
combination of a growth and temperature sine wave to year-length chunks of
the data (see Judd et al., (2018) <doi:10.1016/j.palaeo.2017.09.034>).
This modelling is carried out along a sliding window through the data and
yields estimates of the day of the year (Julian Day) and local growth rate
for each data point. Uncertainties in both modelling routine and the data
itself are propagated and pooled to obtain a confidence envelope around
the age of each data point in the shell. The end result is a shell
chronology consisting of estimated ages of shell formation relative to the
annual cycle with their uncertainties. All formulae in the package serve
this purpose, but the user can customize the model (e.g. number of days in
a year and the mineralogy of the shell carbonate) through input
parameters.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
