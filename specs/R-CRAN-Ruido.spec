%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Ruido
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Soundscape Background Noise, Power, and Saturation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-nortest 
Requires:         R-methods 
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-nortest 

%description
Accessible and flexible implementation of three ecoacoustic indices that
are less commonly available in existing R frameworks: Background Noise,
Soundscape Power and Soundscape Saturation. The functions were design to
accommodate a variety of sampling designs. Users can tailor calculations
by specifying spectrogram time bin size, amplitude thresholds and
normality tests. By simplifying computation and standardizing reproducible
methods, the package aims to support ecoacoustics studies. For more
details about the indices read Towsey (2014)
<doi:10.1016/j.procs.2014.05.063> and Burivalova (2017)
<doi:10.1111/cobi.12968>.

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
