%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  apsimeval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation, Visualisation and Sensitivity Analysis of 'APSIM' Classic Output

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-grDevices 

%description
Reads Agricultural Production Systems sIMulator ('APSIM') Classic 7.x
'.out' files, pairs simulated series with sparse observed measurements,
and computes the goodness-of-fit statistics used in crop-model calibration
and validation, including the decomposition of root mean squared error
into systematic and unsystematic components. Produces publication grade
figures with 'ggplot2': one-to-one scatter plots, residual and Taylor
diagrams, probability of exceedance curves, multi-variable timelines with
a secondary axis, and distribution plots, assembled into multi-panel
figures at journal column widths in colour, greyscale or line art.
Treatment structure encoded in simulation names is parsed into factor
columns, and the sensitivity of an output to those factors is quantified
by variance decomposition, one-at-a-time analysis or range screening. A
built-in 'shiny' interface watches the output directory and refreshes
incrementally as 'APSIM' regenerates its files.

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
