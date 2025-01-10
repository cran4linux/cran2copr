%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ElectDecomp
%global packver   0.0.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Decomposition of Seats-to-Votes Distortions

License:          EPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Analyses districted electoral systems of any magnitude by computing
district-party conversion ratios and seats-to-votes deviations,
decomposing the sources of deviation. Traditional indexes are also
computed. References: Kedar, O., Harsgor, L. and Sheinerman, R.A. (2016).
<doi:10.1111/ajps.12225>. Penades, A and Pavia, J.M. (2025) ''The
decomposition of seats-to-votes distortion in elections: mean, variance,
malapportionment and participation''. Acknowledgements: The authors wish
to thank Consellería de Educación, Cultura, Universidades y Empleo,
Generalitat Valenciana (grant CIACO/2023/031) for supporting this
research.

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
