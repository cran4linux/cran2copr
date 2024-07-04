%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dropR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dropout Analysis by Condition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-lifecycle 

%description
Analysis and visualization of dropout between conditions in surveys and
(online) experiments. Features include computation of dropout statistics,
comparing dropout between conditions (e.g. Chi square), analyzing survival
(e.g. Kaplan-Meier estimation), comparing conditions with the most
different rates of dropout (Kolmogorov-Smirnov) and visualizing the result
of each in designated plotting functions. Sources: Andrea Frick,
Marie-Terese Baechtiger & Ulf-Dietrich Reips (2001)
<https://www.researchgate.net/publication/223956222_Financial_incentives_personal_information_and_drop-out_in_online_studies>;
Ulf-Dietrich Reips (2002) "Standards for Internet-Based Experimenting"
<doi:10.1027//1618-3169.49.4.243>.

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
