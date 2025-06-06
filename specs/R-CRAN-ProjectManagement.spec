%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ProjectManagement
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Management of Deterministic and Stochastic Projects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-triangle 
BuildRequires:    R-CRAN-TUvalues 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-triangle 
Requires:         R-CRAN-TUvalues 
Requires:         R-CRAN-igraph 

%description
Management problems of deterministic and stochastic projects. It obtains
the duration of a project and the appropriate slack for each activity in a
deterministic context. In addition it obtains a schedule of activities'
time (Castro, Gómez & Tejada (2007) <doi:10.1016/j.orl.2007.01.003>). It
also allows the management of resources. When the project is done, and the
actual duration for each activity is known, then it can know how long the
project is delayed and make a fair delivery of the delay between each
activity (Bergantiños, Valencia-Toledo & Vidal-Puga (2018)
<doi:10.1016/j.dam.2017.08.012>). In a stochastic context it can estimate
the average duration of the project and plot the density of this duration,
as well as, the density of the early and last times of the chosen
activities. As in the deterministic case, it can make a distribution of
the delay generated by observing the project already carried out.

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
