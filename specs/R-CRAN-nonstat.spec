%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonstat
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Detecting Nonstationarity in Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Provides a nonvisual procedure for screening time series for
nonstationarity in the context of intensive longitudinal designs, such as
ecological momentary assessments. The method combines two diagnostics: one
for detecting trends (based on the split R-hat statistic from Bayesian
convergence diagnostics) and one for detecting changes in variance (a
novel extension inspired by Levene's test). This approach allows
researchers to efficiently and reproducibly detect violations of the
stationarity assumption, especially when visual inspection of many
individual time series is impractical. The procedure is suitable for use
in all areas of research where time series analysis is central. For a
detailed description of the method and its validation through simulations
and empirical application, see Zitzmann, S., Lindner, C., Lohmann, J. F.,
& Hecht, M. (2024) "A Novel Nonvisual Procedure for Screening for
Nonstationarity in Time Series as Obtained from Intensive Longitudinal
Designs"
<https://www.researchgate.net/publication/384354932_A_Novel_Nonvisual_Procedure_for_Screening_for_Nonstationarity_in_Time_Series_as_Obtained_from_Intensive_Longitudinal_Designs>.

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
