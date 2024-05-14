%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  microdiluteR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Broth Microdilution Assays

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 5.0.1
BuildRequires:    R-tools >= 4.3.3
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-tibble >= 3.2.1
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-rstatix >= 0.7.2
BuildRequires:    R-CRAN-vctrs >= 0.6.5
BuildRequires:    R-CRAN-ggh4x >= 0.2.8
Requires:         R-CRAN-ggthemes >= 5.0.1
Requires:         R-tools >= 4.3.3
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-tibble >= 3.2.1
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-rstatix >= 0.7.2
Requires:         R-CRAN-vctrs >= 0.6.5
Requires:         R-CRAN-ggh4x >= 0.2.8

%description
A framework for analyzing broth microdilution assays in various 96-well
plate designs, visualizing results and providing descriptive and (simple)
inferential statistics (i.e. summary statistics and sign test). The
functions are designed to add metadata to 8 x 12 tables of absorption
values, creating a tidy data frame. Users can choose between clean-up
procedures via function parameters (which covers most cases) or user
prompts (in cases with complex experimental designs). Users can also
choose between two validation methods, i.e. exclusion of absorbance values
above a certain threshold or manual exclusion of samples. A function for
visual inspection of samples with their absorption values over time for
certain group combinations helps with the decision. In addition, the
package includes functions to subtract the background absorption (usually
at time T0) and to calculate the growth performance compared to a
baseline. Samples can be visually inspected with their absorption values
displayed across time points for specific group combinations. Core
functions of this package (i.e. background subtraction, sample validation
and statistics) were inspired by the manual calculations that were applied
in Tewes and Muller (2020) <doi:10.1038/s41598-020-67600-7>.

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
