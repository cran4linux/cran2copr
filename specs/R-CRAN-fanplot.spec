%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fanplot
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualisation of Sequential Probability Distributions Using Fan Charts

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Visualise sequential distributions using a range of plotting styles.
Sequential distribution data can be input as either simulations or values
corresponding to percentiles over time. Plots are added to existing
graphic devices using the fan function. Users can choose from four
different styles, including fan chart type plots, where a set of coloured
polygon, with shadings corresponding to the percentile values are layered
to represent different uncertainty levels. Full details in R Journal
article; Abel (2015) <doi:10.32614/RJ-2015-002>.

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
