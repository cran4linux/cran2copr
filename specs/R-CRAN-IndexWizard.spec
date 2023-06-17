%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IndexWizard
%global packver   0.2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constructing and Analyzing Complex Selection Indices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Allows the construction selection indices based on estimated breeding
values in animal and plant breeding and to calculate several analytic
measures around to assess its impact on genetic and phenotypic progress.
The methodology thereby allows to analyze genetic gain of traits in the
breeding goal which are not part of the actual index and automatically
computes several analytic measures. It further allows to retrospectively
derive realized economic weights from observed genetic trends. The
framework is described in Simianer, H., Heise, J., Rensing, S., Pook, T.
Geibel, J. and Reimer, C. (2023) <doi:10.1186/s12711-023-00807-0>.

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
