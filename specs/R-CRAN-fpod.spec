%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fpod
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Process 'FPOD' and 'CPOD' Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-Rcpp >= 1.1.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Rcpp >= 1.1.0
Requires:         R-CRAN-data.table 

%description
Read 'FPOD' and 'CPOD' data into 'R' directly from the 'FPOD' data files
(i.e. .CP1, .CP3, .FP1 and .FP3 files). The 'FPOD' data files contain
binary data, so they can't trivially be read into 'R' using the usual
approach, e.g. fread() or read.csv(). This package decodes the binary data
and imports all the data in one go (i.e. header/metadata, clicks, 'KERNO'
classifications, environmental data and pseudo-WAV data). It is then
trivial to aggregate data as you please, e.g. detection-positive-minutes
per time block. The advantage of handling data processing in 'R' is a long
topic, but suffice it to say that it 1) simplifies things (many fewer
steps, as different vars have to be exported in multiple goes in the
official 'FPOD' app), and more importantly, 2) makes data processing
transparent and reproducible. References: Pirotta et al. 2014
<doi:10.1111/1365-2435.12146>.

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
