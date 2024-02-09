%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sarp.snowprofile.alignment
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Snow Profile Alignment, Aggregation, and Clustering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sarp.snowprofile >= 1.2.1
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-sarp.snowprofile >= 1.2.1
Requires:         R-CRAN-dtw 
Requires:         R-grid 
Requires:         R-CRAN-data.table 

%description
Snow profiles describe the vertical (1D) stratigraphy of layered snow with
different layer characteristics, such as grain type, hardness, deposition
date, and many more. Hence, they represent a data format similar to
multivariate time series containing categorical, ordinal, and numerical
data types. Use this package to align snow profiles by matching their
individual layers based on Dynamic Time Warping (DTW). The aligned
profiles can then be assessed with an independent, global similarity
measure that is geared towards avalanche hazard assessment. Finally,
through exploiting data aggregation and clustering methods, the similarity
measure provides the foundation for grouping and summarizing snow profiles
according to similar hazard conditions. In particular, this package allows
for averaging large numbers of snow profiles with DTW Barycenter Averaging
and thereby facilitates the computation of individual layer distributions
and summary statistics that are relevant for avalanche forecasting
purposes. For more background information refer to Herla, Horton, Mair,
and Haegeli (2021) <doi:10.5194/gmd-14-239-2021>, and Herla, Mair, and
Haegeli (2022) <doi:10.5194/tc-16-3149-2022>.

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
