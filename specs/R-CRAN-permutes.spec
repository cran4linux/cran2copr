%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  permutes
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Permutation Tests for Time Series Data

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Helps you determine the analysis window to use when analyzing
densely-sampled time-series data, such as EEG data, using permutation
testing (Maris & Oostenveld, 2007) <doi:10.1016/j.jneumeth.2007.03.024>.
These permutation tests can help identify the timepoints where
significance of an effect begins and ends, and the results can be plotted
in various types of heatmap for reporting. Mixed-effects models are
supported using an implementation of the approach by Lee & Braun (2012)
<doi:10.1111/j.1541-0420.2011.01675.x>.

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
