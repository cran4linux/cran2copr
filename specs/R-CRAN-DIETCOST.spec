%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DIETCOST
%global packver   1.0.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate the Cost and Environmental Impact of a Ideal Diet

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-stats 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-magrittr 

%description
Easily perform a Monte Carlo simulation to evaluate the cost and carbon,
ecological, and water footprints of a set of ideal diets. Pre-processing
tools are also available to quickly treat the data, along with basic
statistical features to analyze the simulation results — including the
ability to establish confidence intervals for selected parameters, such as
nutrients and price/emissions. A 'standard version' of the datasets
employed is included as well, allowing users easy access to customization.
This package brings to R the 'Python' software initially developed by
Vandevijvere, Young, Mackay, Swinburn and Gahegan (2018)
<doi:10.1186/s12966-018-0648-6>.

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
