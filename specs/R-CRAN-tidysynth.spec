%global __brp_check_rpaths %{nil}
%global packname  tidysynth
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tidy Implementation of the Synthetic Control Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-LowRankQP 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-LowRankQP 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-optimx 
Requires:         R-stats 

%description
A synthetic control offers a way of evaluating the effect of an
intervention in comparative case studies. The package makes a number of
improvements when implementing the method in R. These improvements allow
users to inspect, visualize, and tune the synthetic control more easily. A
key benefit of a tidy implementation is that the entire preparation
process for building the synthetic control can be accomplished in a single
pipe. For more information on the synthetic control method, see Abadie et
al. (2003) <doi:10.1257/000282803321455188>.

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
