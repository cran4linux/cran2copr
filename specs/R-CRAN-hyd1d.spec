%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hyd1d
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          1d Water Level Interpolation along the Rivers Elbe and Rhine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix >= 3.0.0
BuildRequires:    R-CRAN-RJSONIO >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-plotrix >= 3.0.0
Requires:         R-CRAN-RJSONIO >= 1.0.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-Rdpack 

%description
An S4 class and several functions which utilize internally stored datasets
and gauging data enable 1d water level interpolation. The S4 class
(WaterLevelDataFrame) structures the computation and visualisation of 1d
water level information along the German federal waterways Elbe and Rhine.
'hyd1d' delivers 1d water level data - extracted from the 'FLYS' database
- and validated gauging data - extracted from the hydrological database
'HyDaBa' - package-internally. For computations near real time gauging
data are queried externally from the 'PEGELONLINE REST API'
<https://pegelonline.wsv.de/webservice/dokuRestapi>.

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
