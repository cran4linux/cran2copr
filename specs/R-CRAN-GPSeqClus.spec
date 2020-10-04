%global packname  GPSeqClus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Sequential Clustering Algorithm for Location Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.extras 
BuildRequires:    R-CRAN-plotKML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.extras 
Requires:         R-CRAN-plotKML 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spacetime 
Requires:         R-stats 
Requires:         R-CRAN-suncalc 
Requires:         R-tcltk 
Requires:         R-utils 

%description
Applies sequential clustering algorithm to animal location data based on
user-defined parameters and appends results to the dataframe. Plots
interactive cluster maps and provides a summary dataframe with attributes
for each cluster commonly used as covariates in subsequent modeling
efforts. Additional functions provide individual keyhole markup language
plots for quick assessment, and export global positioning system exchange
format files for navigation purposes.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
