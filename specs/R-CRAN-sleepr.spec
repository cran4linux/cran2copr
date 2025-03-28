%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sleepr
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Activity and Sleep Behaviour

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-behavr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-behavr 
Requires:         R-CRAN-data.table 

%description
Use behavioural variables to score activity and infer sleep from bouts of
immobility. It is primarily designed to score sleep in fruit flies from
Drosophila Activity Monitor (TriKinetics) and Ethoscope data. It
implements sleep scoring using the "five-minute rule" (Hendricks et al.
(2000) <DOI:10.1016/S0896-6273(00)80877-6>), activity classification for
Ethoscopes (Geissmann et al. (2017) <DOI:10.1371/journal.pbio.2003026>)
and a new algorithm to detect when animals are dead.

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
