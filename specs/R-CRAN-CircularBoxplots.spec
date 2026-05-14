%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CircularBoxplots
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Grouped Boxplots for Circular Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plot3D 
Requires:         R-grDevices 

%description
Plotting functions to create circular boxplots for grouped data. The
primary 2-dimensional version creates concentric circular boxplots for
specified groups, scaling the width of each boxplot to adjust for human
perception. The 3-dimensional version maps these plots onto a torus which
is suitable for periodic circular data such as wind direction over the
course of a year. An example dataset of this type is provided for
reference. For examples of circular boxplots and additional implementation
details, see Berlinski et al. (2026) <doi:10.48550/arXiv.2602.05335>.

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
