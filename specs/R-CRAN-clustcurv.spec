%global __brp_check_rpaths %{nil}
%global packname  clustcurv
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Determining Groups in Multiples Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-Gmedian 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-npregfast 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-Gmedian 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-npregfast 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 

%description
A method for determining groups in multiple curves with an automatic
selection of their number based on k-means or k-medians algorithms. The
selection of the optimal number is provided by bootstrap methods. The
methodology can be applied both in regression and survival framework.
Implemented methods are: Grouping multiple survival curves described by
Villanueva et al. (2018) <doi:10.1002/sim.8016>.

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
