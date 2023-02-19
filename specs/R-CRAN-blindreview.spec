%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blindreview
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Blind Review Using Forward Search Procedures

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.7.2
BuildRequires:    R-CRAN-forsearch >= 3.1.0
Requires:         R-CRAN-Hmisc >= 4.7.2
Requires:         R-CRAN-forsearch >= 3.1.0

%description
Randomly assigns identification to one of the variables of the dataset,
say Treatment, and assigns random numbers to all the observations of the
dataset. Reorders the database according to the random numbers, and then
runs the appropriate forward search function on the blinded dataset. A
file is created from which the user can identify any outliers using the
graphics function in this package. An unmasking function is provided so
that the user can identify the potential outliers in terms of their
original values when blinding is no longer needed. Details of the forward
search functions may be found in
<https://CRAN.R-project.org/package=forsearch>.

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
