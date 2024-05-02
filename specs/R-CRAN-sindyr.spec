%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sindyr
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Identification of Nonlinear Dynamics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-arrangements 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-arrangements 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-pracma 

%description
This implements the Brunton et al (2016; PNAS
<doi:10.1073/pnas.1517384113>) sparse identification algorithm for finding
ordinary differential equations for a measured system from raw data
(SINDy). The package includes a set of additional tools for working with
raw data, with an emphasis on cognitive science applications (Dale and
Bhat, 2018 <doi:10.1016/j.cogsys.2018.06.020>). See
<https://github.com/racdale/sindyr> for examples and updates.

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
